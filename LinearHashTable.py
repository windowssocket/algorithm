class LinearHashTable(object):

    def __init__(self, N):
        self.N = N
        self.M = 10
        self.key = []
        self.value = []

        for x in range(self.M):
            self.key.append(None)
            self.value.append(None)

    def put(self,key, value):
        val = hash(key) % self.M
        i = 1
        while self.key[val] is not None:
            val = (i+hash(key)) % self.M
            i += 1
        self.key[val] = key
        self.value[val] = value
        self.N += 1

    def get(self,key):
        val = hash(key) % self.M
        i = 1
        while self.key[val] != key:
            if self.key[val] is not None:
                val = (i+hash(key)) % self.M
                i += 1
            else:
                return None
        return self.value[val]

    def delete(self, key):
        val = hash(key) % self.M
        i = 0
        while self.key[val] != key:
            if self.key[val] is not None:
                i += 1
                val = (i+hash(key)) % self.M
            else:
                return None
        j = val + 1
        re = self.value[val]
        self.key[val] = None
        self.value[val] = None

        rightkey = []
        rightvalue = []

        while self.key[j] is not None:
            rightkey.append(self.key[j])
            rightvalue.append(self.value[j])
            self.key[j] = self.value[j] = None
            j += 1

        for i, x in enumerate(rightkey):
            self.put(x, rightvalue[i])
        return re

a = LinearHashTable(0)
a.put(1,3)
a.put(11,13)
a.put(2,4)
a.put(3,5)

print a.get(1)
print a.get(11)
print a.delete(1)
