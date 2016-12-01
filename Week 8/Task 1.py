class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

class WeightedGraph:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def add_edge(self, node1, node2, weight):
        if node1 not in self.vert_dict:
            self.add_vertex(node1)
        if node2 not in self.vert_dict:
            self.add_vertex(node2)

        self.vert_dict[node1].add_neighbor(self.vert_dict[node2], weight)
        self.vert_dict[node2].add_neighbor(self.vert_dict[node1], weight)

        
if __name__ == '__main__':

    g = WeightedGraph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 5)  
    g.add_edge('a', 'c', 7)
    g.add_edge('a', 'f', 12)
    g.add_edge('b', 'c', 8)
    g.add_edge('b', 'd', 13)
    g.add_edge('c', 'd', 9)
    g.add_edge('c', 'f', 12)
    g.add_edge('d', 'e', 4)
    g.add_edge('e', 'f', 10)

    for v in g:
        for w in v.adjacent.keys():
            print('( %s , %s, %3d)'  % ( v.id, w.id, v.adjacent[w]))

    for v in g:
        print(str(v.id) + ' adjacent: ' + str([x.id for x in v.adjacent]))
