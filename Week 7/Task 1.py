class Graph:
    def __init__(self):
        self.graph = {} ##Create new dictioanry

    def addNode(self, label):
        self.graph[label] = []

    def addEdge(self, n1, n2): ##Adding the edge to each nodes list of edges
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    def printGraph(self): ##Looping through the graph to print all the keys
        for key,value in self.graph.items():
            print(key ,"|", value)


if __name__ == '__main__':

    g = Graph()

    g.addNode('A')
    g.addNode('B')
    g.addNode('C')
    g.addNode('D')
    g.addNode('E')
    g.addNode('F')
    g.addEdge('A','B')
    g.addEdge('A','C')
    g.addEdge('C','D')
    g.addEdge('C','F')
    g.addEdge('C','E')
    g.addEdge('A','D')
    g.addEdge('D','E')
    g.addEdge('A','F')

    g.printGraph()
