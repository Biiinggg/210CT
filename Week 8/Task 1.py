'''Sucsessfully added weights to edges, could not implement Dijksatr'''

import math

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

    '''Attempted implementing Dijkstra using pseudocode from the lecture'''
    def dijkstra(self,start,end):
        v = start
        for node in self.vert_dict:
            node.tw = math.inf
        start.tw = 0
        visited = []
        while v != end:
            for u in self.vert_dict[v]:
                if v.tw + v[u][1] < u.tw:
                    u.tw = v.tw + v[u][1]
                    u.prev = v
            visited.append(v)
        minimum = math.inf
        for n in self.vert_dict:
            if n not in seen and n.tw < minimum:
                v = n
                minimum = n.tw
     
if __name__ == '__main__':

    g = WeightedGraph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')

    g.add_edge('A', 'B', 5)  
    g.add_edge('A', 'C', 7)
    g.add_edge('A', 'F', 12)
    g.add_edge('B', 'C', 8)
    g.add_edge('B', 'D', 13)
    g.add_edge('C', 'D', 9)
    g.add_edge('C', 'F', 12)
    g.add_edge('D', 'E', 4)
    g.add_edge('E', 'F', 10)

    for v in g:
        for w in v.adjacent.keys():
            print('( %s , %s, %3d)'  % ( v.id, w.id, v.adjacent[w]))

    for v in g:
        print(str(v.id) + ' adjacent: ' + str([x.id for x in v.adjacent]))

    #g.dijkstra('A','B') ##Not working
