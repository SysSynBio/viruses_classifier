#! /usr/bin/python
# -*- coding: utf-8 -*-

# todo zmienić nazwę


import os
import json
import cPickle as pickle
from libs.get_feature_indices import _get_feature_indices

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR_PATH, 'conf.json')))
ACID_TO_NUMBER = {'dna':1.0, 'rna':0.0}
NUM_TO_CLASS = {0:'Eucaryota-infecting', 1:'phage'}
feature_indices = {
    classifier_name:_get_feature_indices(pickle.load(open(os.path.join(DIR_PATH, 'files', CONFIG['all_features_file']))),
                              json.load(open(os.path.join(DIR_PATH, 'files', CONFIG['features_file'])))[classifier_name])
    for classifier_name in ('qda', 'knn', 'svc')
}
classifier_paths = {classifier_name:os.path.join(DIR_PATH, 'files', CONFIG['classifier_files'][classifier_name]) for
classifier_name in ('qda', 'knn', 'svc')}
scaler_path = os.path.join(DIR_PATH, 'files', CONFIG['scaler_file'])
