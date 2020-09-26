# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def DFS(g, u, discovered):
  """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

  discovered is a dictionary mapping each vertex to the edge that was used to
  discover it during the DFS. (u should be "discovered" prior to the call.)
  Newly discovered vertices will be added to the dictionary as a result.
  """
  current = u  #current vertex
  previous = None #previuous vertex (vertex that made me discover current vertex)
  while current is not None:
    next = next_discover(g,current, discovered) # tuple new v,e where v is the vertex to discover and a discovery edge
    if next is not None:
      previous = current #save the current vertex in previous, before updating it
      current = next[0] #update current vertex
      discovered[current] = next[1] #add new discovered edge
    else: #if i cannot visit new vertex from current vertex, i return to previous vertex
      current = previous #come back to previous vertex
      if current and discovered[current] is not None: #control that the current vertex is not the root
        previous = discovered[current].opposite(current)
      else: # if the vertex is the root, than its previous is None
        previous = None


def next_discover(g,u,discovered):
  """
  Perform discovery of next unvisited vertex from a given vertex. Return a tuple v, e, where v is the
  unvisited vertex and e is the discovery edge. If it cannot discover a new unvisited vertex, returns None.
  """
  next = None
  for e in g.incident_edges(u): #verifies if i can find a new unexplored edge between u outgoings
    v = e.opposite(u)
    if v not in discovered:
      next = v, e
      break #if i find a new unvisited vertex, i can stop the cycle
  return next


def DFS_complete(g):
  """Perform DFS for entire graph and return forest as a dictionary.

  Result maps each vertex v to the edge that was used to discover it.
  (Vertices that are roots of a DFS tree are mapped to None.)
  """
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None             # u will be the root of a tree
      DFS(g, u, forest)
  return forest
