def Partition(a, l0, hi):
    p = i = q= l0
    v = a[l0]

    for i in range(l0+1,hi+1):
        if a[i] < v:
            q += 1
            if q != i:
                a[i],a[q] = a[q],a[i]
        if a[i] == v:
            p += 1
            a[i], a[p] = a[p], a[i]
            q += 1
    for x in range(p+1):
        a.insert(q, a.pop(0))
    p = q-p
    q += 1
    return p, q

import random
arr = []
for i in range(10):
    arr.append(random.randint(1, 100))

arr = [74, 74,74,74,15, 6, 24, 78, 65, 27, 74, 23, 74, 90, 77, 93]
print arr



print Partition(arr,0,15)

print arr

