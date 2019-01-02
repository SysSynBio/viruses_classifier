.. -*- mode: rst -*-
viruses_classifier
====
Predicts host of a virus based on its (possibly complete) genomic sequence

Installation
------------

Dependencies
~~~~~~~~~~~~

viruses_classifier requires:

- Python = 2.7
- NumPy >= 1.8.2
- SciPy >= 0.13.3
- scikit-learn = 0.19.2


User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of numpy and scipy,
the easiest way to install viruses_classifier is using ``pip`` ::

    pip install git+https://github.com/wojciech-galan/viruses_classifier.git --user


General issues
*************
kNN classifier may not work on 32-bit python, so stick to the 64-bit one. Also, all of the classifiers were trained with a distinct version of scikit-learn, and may not work for the newer/older ones.

Windows installation issues
*************

Under windows you may encounter problems with installing libraries for linear algebra required by scipy. The recommended solution is to install Anaconda which has a proper version of scikit-learn (for example Anaconda2-4.4.0). Then, in Anaconda console, run::

    conda install qt

and proceed with the above pip command.

Source code
-----------

You can check the latest sources with the command::

    git clone https://github.com/wojciech-galan/viruses_classifier


Usage
-----
    viruses_classifier -h


You have to provide path to the sequence file, nucleic acid type and classifier name. For example:

    viruses_classifier raw_or_FASTA-formatted_sequence_file --nucleic_acid rna --classifier qda

    viruses_classifier raw_or_FASTA-formatted_sequence_file --nucleic_acid rna --classifier lr

In both cases you can provide optional argument --probas for class probabilities. This is a switch, so if you run the command with --probas you will obtain class probabilities and if you don't you will obtain only exact class. You can use one of four trained classifiers: LR, SVC, kNN and QDA.

Citation
--------

# TODO
