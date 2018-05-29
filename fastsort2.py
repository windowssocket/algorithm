class FastSort(object):

    def __init__(self, array):
        self.array = array

    def fastSort(self):
        return self.Sort(self.array, 0, len(self.array)-1)

    def Sort(self, array, left, right):
        if left < right:
            mid = self.Partition(array, left, right)
            self.Sort(array, left, mid-1)
            self.Sort(array, mid+1, right)
            return array

    def Partition(self, array, left, right):
        compare = now = left

        for i in range(left+1, right+1):
            if array[i] < array[compare]:
                now += 1
                if now != i:
                    array[i], array[now] = array[now], array[i]

        array[now],array[compare] = array[compare],array[now]
        return now


import random
arr = []
for i in range(10):
    arr.append(random.randint(1, 100))
print arr

fastSort = FastSort(arr)
print fastSort.fastSort()


