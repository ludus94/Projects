def take_key(elem): #it's used for selecting the key which it applies the sorting with
    return elem[1]

def greedy_solution(g):
    count = 0
    direction = g.is_directed() #it verifies if the graph is undirected or not
    vertices_degree = [] #list used for gathering vertices with own degree
    for v in g.vertices():
        d = g.degree(v, direction) #computation of degree
        vertices_degree.append((v, d))
    vertices_degree.sort(key=take_key, reverse=True) #it sorts the pairs on the weight of degree, if is bigger than other, it is located as first

    while len(vertices_degree) != 0:
        vertex = vertices_degree.pop(0) #extraction of element with max degree
        search = False #variable for tracking if there is a vertex among neighbors of current one that has the software, if no-one hasn't it, we can apply the software, otherwise not
        if vertex[0].get_has_software() == False and vertex[0].get_mark() == 'undone':
            for e in g.incident_edges(vertex[0], direction): #we have to control all the neighbors vertices
                u = e.opposite(vertex[0])
                if u.get_has_software() != False:
                    search = True
            if search != True:
                vertex[0].set_has_software(True) #application of the software
                count += 1 #we count the application of the software
                vertex[0].set_mark('done') #the vertex doesn't have to be considered any more
                for e in g.incident_edges(vertex[0], direction):
                    u = e.opposite(vertex[0])
                    if u.get_mark() == 'undone': #there can be some vertices which have already been taken into account
                       u.set_mark('done') #as we have said at the line 24
    return count
