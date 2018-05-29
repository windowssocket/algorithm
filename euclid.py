def EuclidCal(p, q):
    if q == 0:
        return p
    else:
        r = p % q
        return EuclidCal(q, r)

print EuclidCal(1111111,1234567)