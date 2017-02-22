#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import constants
from libs import sequence_processing

def probas_to_dict(probas, translation_dict):
    """
    Transtorms vector of probabilities to dictionary {"type of virus":probability, ...}
    :param probas:
    :param translation_dict:
    :return:
    """
    return {translation_dict[i]:probas[i] for i in range(len(probas))}

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
    vals = [length, acid_code]
    vals.extend([freqs[k] for k in sorted(freqs)])
    print type (vals), np.array(vals).reshape(1, -1)[:, feature_indices] # TODO remove
    vals = scaller.transform(np.array(vals).reshape(1, -1))[:, feature_indices]
    print type(vals), vals # TODO remove
    if probas:
        clf_val = classifier.predict_proba(vals)[0]
        return probas_to_dict(clf_val, constants.NUM_TO_CLASS)
    return constants.NUM_TO_CLASS[classifier.predict(vals)[0]]
