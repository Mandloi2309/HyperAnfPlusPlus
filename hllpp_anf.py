import networkx as nx

from project.hllpp_counter import HllppCounter

counters = {}


def init(graph):
    for index, node in enumerate(graph.nodes()):
        node_counter = HllppCounter()
        node_counter.add(node)
        counters[node] = node_counter


def union(counter_m, counter_n):
    counter_changes = False
    for i in range(counter_m.m):
        if counter_m.M[i] < counter_n.M[i]:
            counter_m.M[i] = counter_n.M[i]
            counter_changes = True
    return counter_changes


def run(graph):
    t = 0
    counter_changes = True
    while counter_changes:
        counter_changes = False
        size = 0
        for index, node in enumerate(graph.nodes()):
            node_counter = counters[node]
            size += node_counter.size()

        print("The neighbourhood function N({0}): {1}".format(t, int(size)))

        for index, node in enumerate(graph.nodes()):
            node_counter = counters[node]
            neighbors = nx.neighbors(graph, node)
            for neighbor in neighbors:
                changed = union(node_counter, counters[neighbor])
                if changed:
                    counter_changes = True

            counters[node] = node_counter

        t = t + 1
