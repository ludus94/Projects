from Exercise3.graph import Graph
from Exercise3.dfsiterative import DFS_complete

if __name__ == '__main__':
    g = Graph(True)

    # v1 = g.insert_vertex("a")
    # v2 = g.insert_vertex("b")
    # v3 = g.insert_vertex("c")
    # v4 = g.insert_vertex("d")
    # v5 = g.insert_vertex("e")
    #
    # g.insert_edge(v1,v2)
    # g.insert_edge(v1,v3)
    # g.insert_edge(v1,v4)
    # g.insert_edge(v1,v5)
    # g.insert_edge(v2,v3)
    # g.insert_edge(v3,v4)
    # g.insert_edge(v5,v3)

    # v1 = g.insert_vertex(1)
    # v2 = g.insert_vertex(2)
    # v3 = g.insert_vertex(3)
    # v4 = g.insert_vertex(4)
    # v5 = g.insert_vertex(5)
    # v6 = g.insert_vertex(6)
    # v7 = g.insert_vertex(7)
    # v8 = g.insert_vertex(8)
    #
    # g.insert_edge(v1,v3)
    # g.insert_edge(v1,v4)
    # g.insert_edge(v1,v5)
    # g.insert_edge(v2,v3)
    # g.insert_edge(v2,v5)
    # g.insert_edge(v3,v6)
    # g.insert_edge(v4,v6)
    # g.insert_edge(v4,v7)
    # g.insert_edge(v5,v7)
    # g.insert_edge(v8,v6)

    v1 = g.insert_vertex("a")
    v2 = g.insert_vertex("b")
    v3 = g.insert_vertex("c")
    v4 = g.insert_vertex("d")
    v5 = g.insert_vertex("e")

    g.insert_edge(v1,v3)
    g.insert_edge(v1,v2)
    g.insert_edge(v1,v4)
    g.insert_edge(v2,v4)
    g.insert_edge(v3,v4)
    g.insert_edge(v3,v5)
    g.insert_edge(v4,v5)
    g.insert_edge(v5,v1)

    for v in DFS_complete(g):
      print(v)

    print('\n')

    for v in DFS_complete(g):
      print(DFS_complete(g)[v])



