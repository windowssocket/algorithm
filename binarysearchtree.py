class Node(object):
    def __init__(self, key, value, number, left=None, right=None):
        self.key = key
        self.value = value
        self.number = number
        self.left = left
        self.right = right


class BinarySearch(object):

    def __init__(self):
        # create a basic binary tree
        self.left = Node(3, 3, 1)
        self.right = Node(7, 7, 1)
        self.root = Node(5, 5, 3, self.left, self.right)

    def put(self, key, value):
        self.__put__(self.root, key, value)

    def __put__(self, node, key, value):
        if node is None: return Node(key, value, 1)
        else:
            if key < node.key:
                node.left = self.__put__(node.left, key, value)
            elif key > node.key:
                node.right = self.__put__(node.right, key, value)
            elif key == node.key:
                node.value = value
            node.number = self.__size__(node.left) + self.__size__(node.right) + 1
            return node

    def get(self, key):
        return self.__get__(self.root, key)

    def insert(self, list):
        pass

    def min(self):
        self.__min__(self.root)

    def __min__(self, node):
        if node.left is None: return node
        else:
            return self.__min__(node.left)

    def max(self):
        self.__max__(self.root)

    def __max__(self, node):
        if node.right is None:
            return node.right
        else:
            return self.__max__(node.right)

    def size(self):
        return self.__size__(self.root)

    def __size__(self, node):
        if node is not None:
            return node.number
        else:
            return 0

    def DelMin(self):
        self.__DelMin__(self.root)

    def __DelMin__(self, node):
        if node.left == None:  return node.right
        else:
            node.left = self.__DelMin__(node.left)
            node.number = self.__size__(node.left) + self.__size__(node.right) + 1
            return node

    def DelMax(self):
        self.__DelMax__(self.root)

    def __DelMax__(self, node):
        if node.right is not None:
            node.right = self.__DelMax__(node.right)
            node.number = self.__size__(self.left) + self.__size__(self.right) + 1
            return node
        else:
            return node.left

    def delete(self, key):
        self.__delete__(self.root, key)

    def __delete__(self, node, key):
        if node == None: return None
        if key < node.key:
            node.left = self.__delete__(node.left, key)
            self.__size__(self.left) + self.__size__(self.right) + 1
            return node
        elif key > node.key:
            node.right = self.__delete__(node.right, key)
            self.__size__(self.left) + self.__size__(self.right) + 1
            return node
        else:
            if node.right == None: return node.left
            if node.left == None: return node.right
            else:
                right_mini = self.__min__(node.right)
                right_mini.right = self.__DelMin__(node.right)
                right_mini.left = node.left
                self.__size__(self.left) + self.__size__(self.right) + 1
                return right_mini

    def traverse(self):
        self.__traverse__(self.root)

    def __traverse__(self, node):
        if node is not None:
            self.__traverse__(node.left)
            print node.key
            self.__traverse__(node.right)
        else:
            return None

    def floor(self, key):
        pass

    def ceiling(self, key):
        pass

    def __get__(self, node, key):
        if node is None: return None
        else:
            if key == node.key: return node.value
            elif key < node.key: return self.__get__(node.left, key)
            elif key > node.key: return self.__get__(node.right, key)

    def __put2__(self,node, key, value):
        if node is None:
            return Node(key, value, 1)
        else:
            if key < node.key:
                node.left = self.__put2__(node.left, key, value)
            elif key> node.key:
                node.right = self.__put2__(node.right, key, value)
            node.number = self.__size__(node.left) + self.__size__(node.right) + 1
            return node



b = BinarySearch()
b.put(4,4)
b.put(8,8)
b.put(9,9)
b.put(1,1)
b.put(2,2)
b.get
b.traverse()
print '*********'
b.DelMax()
b.traverse()
print '********'
print b.get(2)