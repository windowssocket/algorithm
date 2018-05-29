class MergeSort(object):

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def Sort(self):
        return self.__sort__(self.array)

    def __sort__(self, array):
        if len(array) == 1:
            return array
        else:
            mid = len(array) // 2
            array1 = self.__sort__(array[:mid])
            array2 = self.__sort__(array[mid:])
            a = self.Merge(array1, array2)
            return a

    def Merge(self, array1, array2):
        a = []
        i = j = 0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                a.append(array1[i])
                i += 1
            else:
                a.append(array2[j])
                j += 1

        a.extend(array1[i:])
        a.extend(array2[j:])
        return a


array = [1,4,2,5,6,3,6,3,7,34,1]
mergeSort = MergeSort(array)
print mergeSort.Sort()