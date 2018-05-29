class DirectedGraph(object):

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.bag = []
        for i in range(V):
            self.bag.append([])

    # V1 -> V2
    def addEdge(self, V1, V2):
        self.bag[V1].append(V2)
        self.E += 1

    def printGraph(self):
        for x in range(self.V):
            for y in self.bag[x]:
                print str(x) + '---->' + str(y)


class DFS(object):

    def __init__(self, graph):
        self.graph = graph
        self.parent = []
        self.marked = []
        self.ReversePost = []
        self.stack = []

        for i in range(self.graph.V):
            self.parent.append([])
            self.marked.append(False)
            self.stack.append(False)

        # possible clean up and save config

    # start from vector v
    def __dfs__(self, v):
        if self.marked[v] is False:
            self.stack[v] = True
            self.marked[v] = True
            for x in self.graph.bag[v]:
                self.parent[x] = v
                self.__dfs__(x)
            self.stack[v] = False
            # put in stack
            self.ReversePost.insert(0, v)

    def __cleanup__(self):
        pass



class Kosaraju(object):

    def __init__(self, graph):
        self.graph = graph
        self.reverseGraph = self.__reverseGraph__()
        self.ConnectedGraph = []

    def __kosaraju__(self):
        dfs_reverse = DFS(self.reverseGraph)
        # self.reverseGraph.printGraph()
        dfs = DFS(self.graph)
        for v in range(self.reverseGraph.V):
            if dfs_reverse.marked[v] is False:
                dfs_reverse.__dfs__(v)

        print dfs_reverse.ReversePost

        for i in dfs_reverse.ReversePost:
            if dfs.marked[i] is False:
                dfs.__dfs__(i)
                self.ConnectedGraph.append(dfs.ReversePost)
                dfs.ReversePost = []

        print self.ConnectedGraph

    def ShowConnectedGraph(self):
        print self.ConnectedGraph

    # return the reversed graph
    def __reverseGraph__(self):
        reverseGraph = DirectedGraph(self.graph.V)
        for i in range(self.graph.V):
            for t in self.graph.bag[i]:
                reverseGraph.addEdge(t, i)
        return reverseGraph


# created a dummy graph
g = DirectedGraph(6)
edge = [(0,4), (4,0), (4,2), (3,2), (4,1), (5,4), (2,5), (2,0), (0,3)]
for (x, y) in edge:
    g.addEdge(x, y)

g.printGraph()

# implement kosaraju algorithm
k = Kosaraju(g)
k.__kosaraju__()