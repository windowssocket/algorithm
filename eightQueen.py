from datetime import datetime

class TreeNode(object):
     def __init__(self, parent=None, children=[], layer=0, val=0):
         self.parent = parent
         self.children = children
         self.layer = layer
         self.val = val

class EightQueen(object):

    def __init__(self, number):
        # n queen
        self.number = number

        self.root = TreeNode()

        self.solution = []

        self.solution_number = 0

        self.start_time = datetime.now()

    def getRoot(self):
        return self.root

    def forbidNumber(self, current, layer):
        lis = []
        while current.parent is not None:
            lis.append(current.val)
            lis.extend(self.calcorner(current, layer))
            current = current.parent
        lis = list(set(lis))
        return lis

    def calcorner(self, current, layer):
        lis = []
        if layer + current.val - current.layer <= self.number:
            lis.append(layer + current.val - current.layer)
        if current.val - layer + current.layer > 0:
            lis.append(current.val - layer + current.layer)
        return lis

    def createCurrent(self, current):
        forbidden = self.forbidNumber(current, current.layer+1)
        for i in range(1, self.number+1):
            if i not in forbidden:
                newNode = TreeNode(current, [], current.layer+1, i)
                current.children.append(newNode)

    def createTree(self, node):
        self.createCurrent(node)
        if len(node.children) > 0 and len(node.children) <= self.number:
            for x in node.children:
                self.createTree(x)
        elif len(node.children) > self.number:
            print("something went wrong")
        if node.layer == self.number:
            self.solution_number += 1
            print "solution: "+ str(self.solution_number)
            self.solution.append(self.printSolution(node))

    def create(self):
        self.createTree(self.root)
        timediff = datetime.now()- self.start_time
        print "time difference is:" + str(timediff.total_seconds()) + 's'

    def printSolution(self, current):
        if current.parent is not None:
            self.solution.append(self.printSolution(current.parent))
            print "layer = " + str(current.layer)+", and position=" + str(current.val)
            return (current.layer, current.val)




e = EightQueen(20)
e.create()
print e.solution_number
