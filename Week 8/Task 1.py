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


def dijkstra(graph_dict, start, end):

    # empty dictionary to hold distances
    distances = {} 
    # list of vertices in path to current vertex
    predecessors = {} 
    
    # get all the nodes that need to be assessed
    to_assess = graph_dict.keys() 

    # set all initial distances to infinity
    #  and no predecessor for any node
    for node in graph_dict:
        distances[node] = float('inf')
        predecessors[node] = None
    
    # set the initial collection of 
    # permanently labelled nodes to be empty
    sp_set = []

    # set the distance from the start node to be 0
    distances[start] = 0
    
    # as long as there are still nodes to assess:
    while len(sp_set) < len(to_assess):

        # chop out any nodes with a permanent label
        still_in = {node: distances[node]\
                    for node in [node for node in\
                    to_assess if node not in sp_set]}

        # find the closest node to the current node
        closest = min(still_in, key = distances.get)

        # and add it to the permanently labelled nodes
        sp_set.append(closest)
        
        # then for all the neighbours of 
        # the closest node (that was just added to
        # the permanent set)
        for node in graph_dict[closest]:
            # if a shorter path to that node can be found
            if distances[node] > distances[closest] +\
                       graph[closest][node]['weight']:

                # update the distance with 
                # that shorter distance
                distances[node] = distances[closest] +\
                       graph[closest][node]['weight']

                # set the predecessor for that node
                predecessors[node] = closest
                
    # once the loop is complete the final 
    # path needs to be calculated - this can
    # be done by backtracking through the predecessors
    path = [end]
    while start not in path:
        path.append(predecessors[path[-1]])
    
    # return the path in order start -> end, and it's cost
    return path[::-1], distances[end]
        
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

    dijkstra(g.vert_dict,'a','d')
