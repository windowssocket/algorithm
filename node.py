class Node(object):

    def __init__(self, data=None):

        self.Data = data
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self, array):
        tmp = []
        for x in array:
            tmp.append(Node(x))
        for i,x in enumerate(array):
            if 2*i+2 < len(tmp):
                tmp[i].left = tmp[2*i+1]
                tmp[i].right = tmp[2*i+2]
            else:
                break

    def insert(self, data):
        pass

    def delete(self, data):
        pass


tree = Tree([1,2,3,4,5])

