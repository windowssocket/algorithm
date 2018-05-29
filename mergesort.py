def mergesort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)/2
        array1 = mergesort(array[:mid])
        array2 = mergesort(array[mid:])
        return merge(array1, array2)


def merge(array1, array2):
    i = 0
    j = 0
    tmp = []
    while i < len(array1) and j < len(array2) :
        if array1[i] < array2[j]:
            tmp.append(array1[i])
            i += 1
        else:
            tmp.append(array2[j])
            j += 1
    tmp.extend(array1[i:])
    tmp.extend(array2[j:])
    return tmp

array = [1,2,5,4,6,8,12,3,24,7]
print mergesort(array)


