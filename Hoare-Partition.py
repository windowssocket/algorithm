def Partition(a, lo, hi):
    i = lo
    j = hi
    v = a[lo]
    while True:
        for i in range(i+1, hi+1, 1):
            if a[i] > v: break
            else: i += 1

        for j in range(j, lo, -1):
            if a[j] < v: break
            else: j -= 1

        if i == hi:
            return hi
            break
        if j == lo:
            return lo
            break

        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            a[lo],a[j] = a[j],a[lo]
            return j


import random
arr = []
for i in range(10):
    arr.append(random.randint(1, 100))
print arr

print Partition(arr, 0, 9)
print arr



