
"""
sets up some basic functions and loads up useful data

assume run from Latent-Dirichlet-Allocation/ folder...
"""

import numpy as np
import scipy as sp
import os,sys


from liblda.low2corpus import Low2Corpus


# distances
from scipy.stats.distributions import entropy as spKLdiv
from liblda.math.distances import KLdiv, JSdiv


# Phi based mappings
from liblda.subtopics.hungarian_algorithm import getCostMatrix, find_closest
# Theta  based mappings
from liblda.subtopics.hungarian_algorithm import getCostMatrix2, find_closest2





# data exploration, plotting  and reporting
from liblda.topicviz.show_top import show_top
from liblda.topicviz.show_top import top_words_for_topic
import pylab as p





#####
#####   MAIN SETTINGS FOR DATA SET
######################################################################

DATASET_NAME = "ArXiv16k"

print " LOADING DATA  for: " + DATASET_NAME

DATA_PARENT_DIR="/CurrentPorjects/LatentDirichletAllocation/data/arXiv_as_LOW2/"
VOCAB_FILE = DATA_PARENT_DIR+"vocab.txt"
DOCS_FILE =  DATA_PARENT_DIR+"arXiv_train_docs.txt"
IDS_FILE  =  DATA_PARENT_DIR+"arXiv_train_ids.txt"

######################################################################





# loaders....

# vocab, model and doc2id
tcorpus3 = Low2Corpus(DOCS_FILE)
tcorpus3.setVocabFromList( [w.strip() for w in open(VOCAB_FILE, 'r').readlines() ] )
tcorpus3.doCounts()
id_list =  [w.strip() for w in open(IDS_FILE, 'r').readlines() ]
doc2id = dict(  enumerate(id_list) )


# data
phi1   = np.load("../runs/repeatedT50-1/phi.npy")
theta1 = np.load("../runs/repeatedT50-1/theta.npy")
phi2   = np.load("../runs/repeatedT50-2/phi.npy")
theta2 = np.load("../runs/repeatedT50-2/theta.npy")
phi3   = np.load("../runs/repeatedT50-3/phi.npy")
theta3 = np.load("../runs/repeatedT50-3/theta.npy")



print """
you might want to run these commands:

%run liblda/ILDA/doc_likelyhood_plots.py
"""

#seeded_m2 = find_closest2(thetacut, seeded_theta)


