
def preapared(g):
    solutions=[None]*g.vertex_count()
    for e in g.edges():
        e._element="undone"
    l=list(g.vertices())
    create_solutions(solutions,g,l[0])
    #in the end of create you have solution
    #calculate a global solution
    return find_solution(solutions)

def create_solutions(solutions,g,v):

    if g.degree(v)==1:
        e = next(g.incident_edges(v,g.is_directed()))
        u = e.opposite(v)
        if e._element == 'undone':
            solutions[u.element()] = 1
            solutions[v.element()] = 0
            create_solutions(solutions, g, u)

    if solutions[v.element()]==1:
        """function manage:
                 UD->R, check if deg(u)>1:
                                    recoursive;
                                else 
                                    solution[u]=0
                R->R, nothing
                UR->R, nothing , if solution[u] is None:
                                   solutions[u]=0                  
                edges_manager(v,solutions)         
             """

        for e in g.incident_edges(v,g.is_directed()):

            if e._element == "undone":
                u=e.opposite(v)
                solutions[u.element()]=0
                e._element="resolved"
                if g.degree(u)>1:
                    create_solutions(solutions,g,u)
                    if solutions[u.element()]==1 and solutions[v.element()]!=1:
                     solutions[v.element()]=0
                    elif solutions[u.element()] is None:
                        solutions[u.element()]=0
                        solutions[v.element()]=1
                    elif solutions[u.element()] == 0:
                      solutions[v.element()]=1
                    #e._element="resolved"
            elif e._element =="unresolved" and solutions[(e.opposite(v)).element()] is None:
                solutions[(e.opposite(v)).element()]=0
                e._element="resolved"



        """check su tutti gli edge
            UD-> if deg(u)==1:
                    solution[v]=1
                    solution[u]=0
            edge_manager(v,solutions)
            R->nothing
            (UR=>R)->sol[u]=1             
        """
    else: #in this case solutions[v] is None
        for e in g.incident_edges(v,g.is_directed()):
            u=e.opposite(v)
            if e._element=="undone" and g.degree(u,g.is_directed())==1:
                solutions[v.element()]=1
                solutions[u.element()]=0
                e._element="resolved"
            elif g.degree(u,g.is_directed())>1 and e._element=="undone":
                 e._element="unresolved"
                 create_solutions(solutions,g,u)
                 if solutions[u.element()]==1 and solutions[v.element()]!=1:
                     solutions[v.element()]=0
                 elif solutions[u.element()] is None:
                        solutions[u.element()]=0
                        solutions[v.element()]=1
                 elif solutions[u.element()] == 0:
                      solutions[v.element()]=1
                 e._element="resolved"
        """ 
            UR is equivalent to back
            R   is possible 
            UD  if deg(u)==1:
                    solutions[v]=1
                    solutions[u]=0
                    UD->R
                if deg(u)>1:
                        UD->UR
                        create_solutions(solutions,u)
            alla fine della ricorsione continuare a scandagliare gli edges
        """
def find_solution(solutions):
    print(solutions)
    count=0
    for i in range(0,len(solutions)):
        count=count+solutions[i]
    return count
