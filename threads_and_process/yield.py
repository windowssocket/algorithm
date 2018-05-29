def findprime(n):
    sequence = []
    for i in range(n):
        if isprime(i):
            sequence.append(i)
            yield i
    #print sequence
    #for x in sequence:
    #    yield x

def isprime(n):
    for j in range(2,n):
        if n % j == 0:
            return False
    return True


a = findprime(100)
while True:
    try:
        print next(a)
    except:
        break
