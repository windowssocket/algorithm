def BinarySearch(a, key):
    l0 = 0;
    hi = len(a) - 1
    while (l0 < hi):
        mid  = l0 + (hi-l0)/2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            l0 = mid + 1
        else:
            return mid

    return -1

a = [0,1,2,3,4]
print BinarySearch(a, 2)
