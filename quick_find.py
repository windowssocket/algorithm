class ConnectedGraph(object):

    # how many nodes do we have
    def __init__(self, N):
        tmp = []
        for x in range(N):
            tmp.append(x)
        self.array = tmp

    def isConnected(self, x, y):
        if self.array[x] is self.array[y]:
            return True
        else:
            return False

    def Union(self, x, y):
        if self.isConnected(x, y):
            pass
        else:
            for i in self.array:
                if self.array[i] == self.array[y]:
                    self.array[i] = self.array[x]


class TreeConnectedGraph(object):

    def __init__(self, N):
        tmp = []
        for x in range(N):
            tmp.append(x)
        self.array = tmp

    def Find(self, x):
        header = x
        height = 1
        while self.array[header] is not header:
            header = self.array[header]
            height += 1
        tmp1 = [header, height]
        return tmp1

    def isConnected(self, x, y):
        if self.Find(x)[0] == self.Find(y)[0]:
            return True
        else:
            return False

    def Union(self, x, y):
        if self.isConnected(x, y):
            pass
        else:
            if self.Find(x)[1] <= self.Find(y)[1]:
                self.array[self.Find(x)[0]] = self.array[self.Find(y)[0]]
            else:
                self.array[self.Find(y)[0]] = self.array[self.Find(x)[0]]






N = 10
a = [(1,2),(3,4),(5,6),(1,6)]

graph = TreeConnectedGraph(N)

for x,y in a:
    graph.Union(x,y)
print graph.array

print graph.isConnected(3,5)
print graph.isConnected(2,5)

