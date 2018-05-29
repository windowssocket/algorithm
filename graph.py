class Graph(object):

    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.map = []
        self.stack = []
        for i in range(V):
            self.map.append([])

    def addEdge(self, V1, V2):
        self.map[V1].insert(0, V2)
        self.map[V2].insert(0, V1)

    def AdjNode(self, V1):
        return self.map[V1]

    def AvgDegree(self):
        totalDegree = 0
        for x in self.map:
            totalDegree += len(x)
        totalDegree /= 2
        return totalDegree

    def selfLoop(self):
        totalLoop = 0
        for i, x in enumerate(self.map):
            if i in x:
                totalLoop += x.count(i)
        return totalLoop


class DFS(object):

    def __init__(self, graph, V1):
        self.graph = graph
        self.parent = []
        self.color = []
        self.V1 = V1
        self.stack = []
        self.hasloop = False
        for x in range(graph.V):
            self.color.append(False)
            self.parent.append(None)

    def dfs(self, graph, V1):
        self.color[V1] = True
        for x in graph.map[V1]:
            if self.color[x] is False:
                self.color[x] = True
                self.parent[x] = V1
                self.dfs(graph, x)

    def hasPath(self, graph, V2):
        self.dfs(graph, self.V1)
        return self.color[V2]

    def PathTree(self, V2):
        if V2 != self.V1:
            self.stack.append(V2)
            self.PathTree(self.parent[V2])
        else:
            self.stack.append(self.V1)

    def ShowTree(self):
        for x in self.stack[::-1]:
            print x


class BFS(object):

    def __init__(self, graph, V1):
        self.graph = graph
        self.V1 = V1
        self.color = []
        self.parent = []
        for x in range(graph.V):
            self.color.append(False)
            self.parent.append(None)
        self.queue = [self.V1]

    def bfs(self):
        while len(self.queue) > 0:
            v = self.queue.pop(0)
            self.color[v] = True
            for x in self.graph.map[v]:
                if self.color[x] is False:
                    self.color[x] = True
                    self.queue.append(x)
                    self.parent[x] = v

    def isConnected(self, V2):
        return self.color[V2]

    def shortPath(self, V2):
        self.bfs()
        if self.isConnected(V2):
            x = V2
            while self.parent[x] is not None:
                if self.parent[x] == self.V1:
                    print x
                    print self.parent[x]
                    break
                else:
                    print x
                    x = self.parent[x]
        else:
            print None


class AlgDFS(object):

    def __init__(self, graph):
        self.graph = graph
        self.hasloop = False

    def hasLoop(self):
        for i in range(self.graph.V):
            self.parent = []
            self.color = []
            for x in range(graph.V):
                self.color.append(False)
                self.parent.append(None)
            self.__dfs__(i, i)
        return self.hasloop

    def __dfs__(self, node, compare):
        self.color[node] = True
        for x in self.graph.map[node]:
            if self.color[x] is False:
                self.color[x] = True
                self.parent[x] = node
                self.__dfs__(x, node)
            else:
                if compare != x:
                    self.hasloop = True





graph = Graph(6, 4)
graph.addEdge(1, 2)
graph.addEdge(1, 0)
graph.addEdge(1, 4)
graph.addEdge(0, 5)
graph.addEdge(2, 4)


a = AlgDFS(graph)
print a.hasLoop()

fn = getattr(graph, 'addEdge')
print(fn)



