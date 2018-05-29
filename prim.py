class Element(object):

    def __init__(self, startNode, endNode, weight):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = weight

    def PrintElement(self):
        print(self.startNode)
        print(self.endNode)
        print(self.weight)
        print('***************************')

    def getV2(self):
        return self.endNode

    def getWeight(self):
        return self.weight

    def getV1(self):
        return self.startNode


class WeightGraph(object):

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.bag = []
        for i in range(V):
            self.bag.append([])

    # V1 -> V2 (weight = w)
    def addEdge(self, V1, V2, w=0):
        self.bag[V1].append(Element(V1, V2, w))
        self.E += 1

    def printGraph(self):
        for x in range(self.V):
            for y in self.bag[x]:
                y.PrintElement()

class Prim(object):

    def __init__(self, graph):
        self.graph = graph
        self.PrimTree = []
        self.marked = []
        self.edgeTo = []
        for i in range(self.graph.V):
            self.marked.append(False)

    def cmpElement(self, x, y):
        if x.getWeight() < y.getWeight():
            return -1
        elif x.getWeight() > y.getWeight():
            return 1
        else:
            return 0

    def prim(self, v):
        if self.marked[v] is False:
            self.marked[v] = True
            for x in self.graph.bag[v]:
                w = x.getWeight()
                self.edgeTo.append(Element(v, x.getV2(), w))
                self.RemoveUnused()
                self.edgeTo.sort(self.cmpElement)
                if len(self.edgeTo) > 0:
                    self.PrimTree.append(self.edgeTo.pop(0))
                    self.prim(x.getV2())

    def RemoveUnused(self):
        for x in self.edgeTo:
            if self.marked[x.getV1()] and self.marked[x.getV2()]:
                self.edgeTo.remove(x)

    def getPrim(self):
        if len(self.PrimTree) == self.graph.V - 1:
            print '*** prim  Solution:***'
            for x in self.PrimTree:
                x.PrintElement()
            return self.PrimTree
        else:
            return None


class Kruskal(object):

    def __init__(self, graph):
        self.edgeTo = []
        self.graph = graph
        self.marked = []
        self.KruskalTree = []
        for x in range(self.graph.V):
            self.marked.append(False)
            for y in self.graph.bag[x]:
                self.edgeTo.append(y)

    def cmpElement(self, x, y):
        if x.getWeight() < y.getWeight():
            return -1
        elif x.getWeight() > y.getWeight():
            return 1
        else:
            return 0

    def RemoveUnused(self):
        for x in self.edgeTo:
            if self.marked[x.getV1()] and self.marked[x.getV2()]:
                self.edgeTo.remove(x)

    def kruskal(self):
        self.edgeTo.sort(self.cmpElement)
        for x in self.edgeTo:
            if self.marked[x.getV1()] and self.marked[x.getV2()]:
                #self.edgeTo.remove(x)
                pass
            else:
                self.marked[x.getV1()] = True
                self.KruskalTree.append(x)
        return self.KruskalTree




# created a dummy graph
g = WeightGraph(6)
edge = [(0,4,0.3), (4,0,1), (4,2,0.5), (3,2,0.4), (4,1,0.2), (5,4,0.1), (2,5,0.2), (2,0,0.7), (0,3,0.8)]
for (x, y, w) in edge:
    g.addEdge(x, y, w)

# g.printGraph()

# Prim Algorithm
#prim = Prim(g)
#prim.prim(1)
#prim.getPrim()

kruskal = Kruskal(g)
ret = kruskal.kruskal()

if len(ret) == 5:
    for x in ret:
        x.PrintElement()

