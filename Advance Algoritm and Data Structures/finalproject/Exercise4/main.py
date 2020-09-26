from Exercise4.graph import Graph
from Exercise4.dynamicprogramming import preapared

def main():
   g=Graph()
   v0=g.insert_vertex(0)
   v1=g.insert_vertex(1)
   v2=g.insert_vertex(2)
   v3=g.insert_vertex(3)
   v4=g.insert_vertex(4)
   v5=g.insert_vertex(5)
   v6=g.insert_vertex(6)
   v7=g.insert_vertex(7)
   v8=g.insert_vertex(8)
   v9=g.insert_vertex(9)
   v10=g.insert_vertex(10)
   """g.insert_edge(vA,vB)
   g.insert_edge(vB,vC)
   g.insert_edge(vC,vD)"""
   g.insert_edge(v1,v2)
   g.insert_edge(v1,v3)
   g.insert_edge(v1,v4)
   g.insert_edge(v4,v7)
   g.insert_edge(v4,v8)
   g.insert_edge(v7,v0)
   g.insert_edge(v0,v5)
   g.insert_edge(v0,v6)
   g.insert_edge(v5,v9)
   g.insert_edge(v6,v10)

   print(preapared(g))
if __name__=="__main__":
    main()
