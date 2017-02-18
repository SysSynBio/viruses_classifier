#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import constants
from libs import sequence_processing

def classify(seq, nuc_acid, scaller, classifier, feature_indices, probas=False):
    """
    Classify viral sequence
    :param seq: - sequence in upperrcase. Can contain degenerate nucleotides in IUPAC notation
    :param nuc_acid: either 'dna' or 'rna'
    :param scaller: trained scaller
    :param classifier: trained classifier
    :param feature_indices: indices of selected features
    :param probas: when True function returns class probabilities instead of class
    :return: class code (for example 0 or 1) or class probabilities
    """
    acid_code = constants.ACID_TO_NUMBER[nuc_acid]
    length = len(seq)
    nuc_frequencies = sequence_processing.nucFrequencies(seq, 2)
    nuc_frequencies_ = {'nuc_frequencies__'+key : value for key, value in
                       nuc_frequencies.iteritems()}
    relative_nuc_frequencies_one_strand_ = {'relative_nuc_frequencies_one_strand__'+key : value for key, value in
                                           sequence_processing.relativeNucFrequencies(nuc_frequencies, 1).iteritems()}
    relative_trinuc_freqs_one_strand_ = {'relative_trinuc_freqs_one_strand__'+key : value for key, value in
                                        sequence_processing.thirdOrderBias(seq, 1).iteritems()}
    freqs = nuc_frequencies_
    freqs.update(relative_nuc_frequencies_one_strand_)
    freqs.update(relative_trinuc_freqs_one_strand_)
    vals = [acid_code, length]
    vals.extend([freqs[k] for k in sorted(freqs)])
    print type (vals), vals # TODO remove
    vals = scaller.transform(np.array(vals).reshape(1, -1))[:,feature_indices]
    print type(vals), vals # TODO remove
    if probas:
        return classifier.predict_proba(vals)[0]
    return classifier.predict(vals)[0]
