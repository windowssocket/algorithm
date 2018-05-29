def mergeSort(array):
    if len(array) == 1:
        return array
    elif len(array) > 1:
        mid = len(array)/2
        array1 = mergeSort(array[:mid])
        array2 = mergeSort(array[mid:])
        i = j = 0
        tmp = []
        while i < len(array1) and j < len(array2):
            if array1[i] > array2[j]:
                tmp.append(array2[j])
                j += 1
            elif array1[i] <= array2[j]:
                tmp.append(array1[i])
                i += 1
        tmp.extend(array1[i:])
        tmp.extend(array2[j:])
        return tmp


def binarySearch(array, ele):
    start = 0
    mid = len(array)/2
    end = len(array) - 1
    if ele > array[end] or ele < array[start]:
        return None
    else:
        while start <= end:
            if array[mid] > ele:
                end = mid - 1
                mid = start + (end - start + 1)/2
            elif array[mid] < ele:
                start = mid + 1
                mid = start + (end - start + 1)/2
            elif array[mid] == ele:
                return mid
                break


def threeSum(array):
    sorted_array = mergeSort(array)
    print sorted_array
    tmp = []
    for i in range(len(sorted_array)):
        for j in range(len(sorted_array)):
            print i, j
            ele = -(sorted_array[i] + sorted_array[j])
            print ele
            result = binarySearch(sorted_array, ele)
            if result is not None:
                print "found 3 sum for " + str(i) + str(j) + str(result)
                tmp.append((i,j,result))
            else:
                print result
    if len(tmp) is 0:
        print "nothing found!"
    return tmp



a = [1,2,3,-1,-2,-3]
threeSum(a)