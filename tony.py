# There is no graph, only Zuul.

# Just kidding, here's a simple ring graph because pie charts are evil, but rings...aren't?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ring_graph(size=[1, 2, 3], labels=["A", "B", "C"], title="title", figsize=(8,8), colors=["R", "G", "B"]):
    """
    Really simple ring graph.

    INPUT:
    - size: list of ints; size of the ring sections (relative)
    - labels: list of str; labels of ring sections
    - title: str; name of your ring graph
    - figsize: tuple of ints; xy-size of the graph
    - colors: list of str; list of the colors of your segments

    OUTPUT:
    Should be a ring graph!
    """
    fig, ax = plt.subplots(figsize=figsize)

    labels = labels
    size = size
    colors = colors

    # Create a circle to obscure the center of the pie chart, making it a ring graph:
    my_circle = plt.Circle( (0,0), 0.7, color='white')

    ax.pie(size, labels=labels, colors=colors)
    ax.set_title(title)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
