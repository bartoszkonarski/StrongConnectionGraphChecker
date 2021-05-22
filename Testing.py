# importing networkx 
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np

def Graf():
    G= nx.DiGraph()

    G.add_edges_from(
        [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
         ('B', 'H'), ('B', 'G'), ('B', 'F'),('B', 'F'), ('C', 'G'),
         ('1', '2'), ('5', '1'), ('4', '5'),('1', '3'), ('5', '9')])
    color_map=[]

    # # nx.draw(G,node_color='yellow', with_labels = True, arrows=True)
    # plt.title("Graf nie jest ściśle spójny")
    # pos = nx.circular_layout(G,scale=2) # double distance between all nodes
    # nx.draw(G, pos,node_color='yellow', with_labels = True, arrows=True,arrowsize=15)
    #
    # plt.show()
    print(len(list("ABCDEFGHIJKLMNOPRSTUWXYZ")))

Graf()