class BinaryHeap(object):
    def __init__(self, array):
        array.insert(0, -1)
        self.array = array
        print self.array

    def sink(self, ele):
        return self.__sink(ele, self.array)

    def swim(self, ele):
        return self.__swim(ele, self.array)

    def __swim(self, ele, array):
        number = len(array)
        array.append(ele)
        while number >= 2:
            if ele > array[number/2]:
                array[number],array[number/2] = array[number/2],array[number]
                number /= 2
            else:
                break
        return array

    def larger(self, array, i, j):
        if array[i] > array[j]:
            return i
        else:
            return j

    def __sink(self, ele, array):
        number = len(array)
        array.insert(1, ele)
        start = 1
        while 2*start <= number:
            if 2*start+1 <= number:
                more = self.larger(array, 2*start, 2*start+1)
            else:
                more = 2*start

            if ele < array[more]:
                array[start],array[more] = array[more],array[start]
                start = more
            else:
                break

        return array

    def b_sort(self):
        length = len(self.array)
        i = length - 1
        while i >= 1:
            print self.findMax()
            i -= 1


    def findMax(self):
        max = self.array.pop(1)
        self.array = self.__sink(self.array[-1], self.array[0:-1:1])
        return max

    def printArray(self):
        print self.array

array = [15,7,8,5,6,4,5,1,2]
bheap = BinaryHeap(array)
bheap.swim(12)
bheap.b_sort()








