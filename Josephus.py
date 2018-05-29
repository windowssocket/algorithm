class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Ring(object):

    def __init__(self, n):

        # create ring
        ring = []
        for x in range(n):
            ring.append(Node(x))
        for i, x in enumerate(ring):
            if i < len(ring) - 1:
                ring[i].next = ring[i+1]
        ring[-1].next = ring[0]
        self.head = ring[0]
        self.size = len(ring)

    def delX(self, m):
        # del m-1 element
        if m is 1:
            t = self.size - 1
            print "size = " + str(t)
        elif m > 1 and m <= self.size:
            t = m - 2 # one ele ahead
        else:
            print ("error")
        pointer = self.head
        while t > 0:
            pointer = pointer.next
            t -= 1
        tmp = pointer.next
        pointer.next = tmp.next
        self.size -= 1
        self.head = pointer.next
        return tmp.data

    def printX(self):
        # print
        pointer = self.head
        for x in range(self.size):
            print pointer.data
            print '*****'
            pointer = pointer.next

    def calculate(self,m):
        while self.size > 1:
            print self.delX(m)
            print 'killed'
        print 'only one left with' + str(self.head.data)


class Josephus:

    def __init__(self, n, m):
        self.n = n
        self.m = m

    def cal(self):
        r = Ring(self.n)
        r.calculate(self.m)

j = Josephus(5,2)
j.cal()










