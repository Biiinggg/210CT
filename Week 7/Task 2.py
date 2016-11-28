class Node:
    def __init__(self, n):
        self.label = n
        self.edges = list()

    def addEdges(self, v):
        self.edges.append(v)

class Graph:
    graph = {} ##Create new dictioanry

    def addNode(self, node):
        self.graph[node.label] = node

    def addEdge(self, u, v): ##Adding the edge to each nodes list of edges
        self.graph[u].addEdges(v)
        self.graph[v].addEdges(u)


    def printGraph(self): ##Looping through the graph to print all the keys
        for key in sorted(list(self.graph.keys())):
            print(key + str(self.graph[key].edges))

def depth_first_search(G,v):
    s = ()
    visited = []
    s.push(v)
    while(s!=None):
        u=s.pop()
        if u is not visited:
            visited.append(u)
            for all edges, e, from u, s.push(e.to)

def breadth_first_search(G,v):
    q = ()
    visited = []
    q.enqueue(v)
    while(q!=None):
        u=q.dequeue()
        if u is not in visited:
            visited.append(u)
        for all edges, e, from u:
            q.enqueue(e.to)
        return visited


g = Graph()

g.addNode(Node('A'))
g.addNode(Node('B'))
g.addNode(Node('C'))
g.addEdge('A','B')
g.addEdge('A','C')

g.printGraph()
