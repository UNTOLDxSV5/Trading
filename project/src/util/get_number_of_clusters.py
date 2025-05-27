# utils.py
import numpy as np

def get_number_of_clusters(labels):
    return len(np.unique(labels))
