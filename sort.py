class Sort(object):

    def __init__(self, array):
        self.array = array

    def selection(self, array):
        for i in range(len(array)):
            start = i
            for j, x in enumerate(array[i:]):
                if x < array[start]:
                    start = i + j
            tmp = array[i]
            array[i] = array[start]
            array[start] = tmp

        return array

    def insert(self, array):
        for i in range(1, len(array)):
            for j in range(1,i+1):
                if array[i] > array[i-j]:
                    value = array.pop(i)
                    array.insert(i-j+1, value)
                    break
        return array






a = [1,4,2,5,3,6,5]
s = Sort(a)
# print s.selection(a)
print s.insert(a)



