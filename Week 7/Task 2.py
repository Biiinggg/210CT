class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

'''Generic Queue and Stack class to enable competion of task
    https://interactivepython.org'''
  
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
    
    def depth_first_search(self,v):
        s = Stack()
        visited = []
        s.push(v)
        while s.isEmpty() == False:
            u = s.pop()
            if u is not visited:
                visited.append(u)
                for edge in self.graph[u]:
                    s.push(edge)
            file = open("depth_first_search_output.txt","w")
            file.write(str(visited))
            file.close
            return visited

    def breadth_first_search(self,v):
        q = Queue()
        visited = []
        q.enqueue(v)
        while q.isEmpty() == False:
            u = q.dequeue()
            if u not in visited:
                visited.append(u)
            for edge in self.graph[u]:
                q.enqueue(edge)
            file = open("breadth_first_search_output.txt","w")
            file.write(str(visited))
            file.close
            return visited

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

    print(g.depth_first_search('D'))
    print(g.breadth_first_search('A'))

