
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd

import dgl
from dgl.data import MiniGCDataset


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():
    
    g_nx  = nx.petersen_graph()
    g_dgl = dgl.DGLGraph(g_nx)

    plt.figure()
    #plt.subplot(121)
    #nx.draw(g_nx, with_labels=True)
    #plt.subplot(122)
    #nx.draw(g_dgl.to_networkx(), with_labels=True)
    #plt.show()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if (__name__ == "__main__"):
    main()