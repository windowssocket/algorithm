class Node(object):

    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

    def contain(self, key):
        if key == self.key:
            return True
        return False


class LinkedHashTable(object):

    def __init__(self, ran):
        self.range = ran
        set = []
        for x in range(self.range):
            set.append(None)
        self.set = set

    def HashFunction(self, key):
        return key % self.range

    def put(self, key, value):
        val = self.HashFunction(key)
        x = self.set[val]
        if x is None:
            self.set[val] = Node(key, value)
        else:
            while x.next is not None:
                if x.contain(key):
                    x.val = val
                    return True
                else:
                    x = x.next
            x.next = Node(key, value)
        return True

    def get(self, key):
        val = self.HashFunction(key)
        x = self.set[val]
        while x is not None:
            if x.contain(key):
                return x.val
            else:
                x = x.next
        return None

    def delete(self, key):
        val = self.HashFunction(key)
        x = self.set[val]
        parent = None
        while x is not None:
            if x.contain(key):
                if parent is not None:
                    parent.next = x.next
                else:
                    self.set[val] = x.next
                return x
            else:
                parent = x
                x = x.next
        return None


a = LinkedHashTable(10)
for i in range(40):
    a.put(i, i+2)

print a.get(30)
print a.get(20)
print a.delete(10).val
print a.delete(0).val
print a.set[0].val

print hash((1,2,3,4,5))




