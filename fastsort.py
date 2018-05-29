class FastSort(object):

    def __init__(self, array):
        self.array = array
        self.len = len(array)

    def Sort(self):
        return self.__sort__(self.array)

    def __sort__(self, array):
        if len(array) < 1:
            return array
        else:
            split = self.Split(array)
            self.__sort__(array[:split-1])
            self.__sort__(array[split+1:])
            return array

    def Split(self, a):
        left = 0
        for x in range (1, len(a)):
            if a[x] < a[0]:
                left += 1
                if left != x:
                    a[left],a[x] = a[x],a[left]
        a[0],a[left] = a[left],a[0]
        return left


array = [20,4,5,20,23,2,5,6,3,89,3,7,34,1]
print array
fastSort = FastSort(array)
print fastSort.Sort()
