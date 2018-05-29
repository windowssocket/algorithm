class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class NodeStack(object):

    def __init__(self, array):
        tmp = []
        for x in array:
            a = Node(x)
            tmp.append(a)
        for i,x in enumerate(tmp):
            if i<len(tmp)-1:
                x.next = tmp[i+1]
        self.head = tmp[0]
        self.size = len(tmp)

    def printx(self):
        start = self.head
        while start.next is not None:
            print start.data
            print "*****"
            start = start.next
        # print the last one
        print start.data
        print ("finish")

    def insertx(self, position, data):
        x = Node(data)
        if position == 0:
            x.next = self.head
            self.head = x
            self.size += 1
        else:
            i = position - 1
            tmp = self.head
            while i > 0:
                tmp = tmp.next
                i -= 1
            record = tmp.next
            tmp.next = x
            x.next = record
            self.size += 1

    def delx(self, position):
        if position == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            i = position - 1
            tmp = self.head
            while i > 0:
                tmp = tmp.next
                i -= 1
            record = tmp.next
            tmp.next = record.next
            self.size -= 1

    def sizex(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        return False








array = [1,2,3,4,5]
nodestack = NodeStack(array)
nodestack.printx()
nodestack.delx(4)
nodestack.printx()
print nodestack.sizex()



