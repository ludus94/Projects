import random

from Exercise5.graph import Graph
from Exercise5.greedy_solution import greedy_solution


def main():

    for j in range(1, 101):
        g = Graph()
        for i in range(1, 101):
            g.insert_vertex(i)
        for u in g.vertices():
            for v in g.vertices():
                if (random.getrandbits(1) == True) and (u != v) and g.get_edge(u, v) == None:
                    g.insert_edge(u, v)
        c = greedy_solution(g)
        print('There are ' + str(c) + ' installed software in the ' + str(j) + '-th graph\n')

if __name__ == '__main__':
    main()
