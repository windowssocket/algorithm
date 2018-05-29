class DirectGraph(object):

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.bag = []
        for x in range(V):
            self.bag.append([])

    # V1->V2
    def addEdge(self, V1, V2):
        self.bag[V1].append(V2)
        self.E += 1

    def deleteEdge(self, V1, V2):
        if V2 in self.bag[V1]:
            self.bag.remove(V2)

    def adj(self, V1):
        return self.bag[V1]


class DirectDFS(object):

    def __init__(self, graph):
        self.stack = []
        self.graph = graph
        self.parent = []
        self.mark = []
        self.hasloop = False
        self.loops = []
        for x in range(self.graph.V):
            self.parent.append(None)
            self.mark.append(False)
            self.stack.append(False)

    def DFS(self, v):
        if self.mark[v] is False:
            self.stack[v] = True
            self.mark[v] = True
            for x in self.graph.bag[v]:
                if self.mark[x] is False:
                    self.parent[x] = v
                    self.DFS(x)
                elif self.stack[x] == True:
                    self.hasloop = True
                    y = v
                    loop = []
                    while y is not x:
                        if self.parent[y] is not None:
                            loop.append(y)
                            y = self.parent[y]
                    loop.append(x)
                    self.loops.append(loop)
        self.stack[v] = False

    def isConnected(self, V1, V2):
        self.DFS(V1)
        return self.mark[V2]

    def ShowPath(self, V1, V2):
        self.DFS(V1)
        if self.isConnected(V1, V2):
            x = V2
            while self.graph.bag[x] is not V1:
                print x
            print V1

    def ShowLoop(self):
        for x in range(self.graph.V):
            if self.mark[x] is False:
                self.DFS(x)
                self.parent = []
                self.stack = []
                for x in range(self.graph.V):
                    self.parent.append(None)
                    self.stack.append(False)
        return self.loops

    def hasLoop(self):
        return self.hasloop


class DepthFistGraph(DirectDFS):

    def __init__(self, graph):
        super(DepthFistGraph, self).__init__(graph)
        self.pre = []
        self.post = []
        self.poststack = []

    def dfs(self, v):
        if self.mark[v] is False:
            self.mark[v] = True
            self.pre.append(v)
            for x in self.graph.bag[v]:
                if self.mark[x] is False:
                    self.parent[x] = v
                    self.dfs(x)
            self.post.append(v)
            self.poststack.insert(0, v)

    def __dfs__(self, v, graph):
        if self.mark[v] is False:
            self.mark[v] = True
            self.pre.append(v)
            for x in graph.bag[v]:
                if self.mark[x] is False:
                    self.parent[x] = v
                    self.dfs(x, graph)
            self.post.append(v)
            self.poststack.insert(0, v)

    def prequeue(self):
        return self.pre

    def postqueue(self):
        return self.post

    def showpoststack(self):
        return self.poststack

    def reverseGraph(self):
        newgraph = DirectGraph(self.graph.V)
        for x in range(self.graph.V):
            for y in self.graph.bag[x]:
                newgraph.addEdge(y, x)
        return newgraph

    def kosaraju(self):
        reversegraph = self.reverseGraph()
        self.__dfs__(1, reversegraph)
        return self.poststack










graph = DirectGraph(6)
graph.addEdge(1, 2)
graph.addEdge(1, 0)
graph.addEdge(1, 4)
graph.addEdge(0, 5)
graph.addEdge(2, 4)
graph.addEdge(4, 0)

a = DepthFistGraph(graph)
a.dfs(1)
print a.prequeue()
print a.postqueue()
print a.showpoststack()

print a.reverseGraph()
print a.kosaraju()







