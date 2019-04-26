import numpy as np
from data import *

# Is this how you do it?
d = create_dictionary.main()

def PageRank(data, weight_dict):
    """ This is our pagerank algorithm.

    Inputs:
        data: a dictionary --
                key: name
                value: list of Meet objects
        weight_dict: a dictionary --
                key: competition name
                value: weight of an edge corresponding to that competition

    Returns:
        The invariant distribution.

    """
    P = np.zeros([len(data), len(data)])
    swimmer_indices = {}
    i = 0
    for key in data:
        if key not in swimmer_indices:
            swimmer_indices[key] = i
            i += 1
        for m in data[key]:
            for swimmer in m.lost_to:
                if swimmer not in swimmer_indices:
                    swimmer_indices[swimmer] = i
                    i += 1
                P[swimmer_indices[key]][swimmer_indices[swimmer]] += weight_dict[m.name]

    w, v = np.linalg.eig(P.T)
    return v[0]
