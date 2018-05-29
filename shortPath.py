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


class Dijkastra(object):
    def __init__(self, graph, startNode):
        self.graph = graph
        self.edgeTo = []
        self.pq = [startNode]
        for x in xrange(self.graph.V):
            # initial using -1
            self.edgeTo.append(Element(-1, -1, 1000000))
        self.edgeTo[startNode] = Element(0, 0, 0)

    def dijkastra(self):
        while len(self.pq) > 0:
            v = self.pq.pop(0)
            for x in self.graph.bag[v]:
                if self.edgeTo[x.getV2()].getWeight() > self.edgeTo[v].getWeight() + x.getWeight():
                    self.edgeTo[x.getV2()] = Element(v, x.getV2(), self.edgeTo[v].getWeight() + x.getWeight())
                if self.pq.count(x.getV2()) == 0:
                    self.pq.append(x.getV2())

    def SPT(self):
        for x in self.edgeTo:
            x.PrintElement()



g = WeightGraph(6)
edge = [(0,4,0.3), (3,2,0.4), (4,1,0.2), (5,4,0.1), (5,2,0.2), (0,2,0.7), (0,3,0.8)]
for (x, y, w) in edge:
    g.addEdge(x, y, w)

d = Dijkastra(g, 0)
d.dijkastra()
d.SPT()