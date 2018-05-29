import datetime

class Shell(object):

    def __init__(self, array):
        self.array = array
        self.length = len(array)
        h = 1
        shell_var = [1]
        while 3*h < self.length:
            h = 3*h + 1
            shell_var.insert(0,h)

        s = 1
        test_var = [1]
        while 10**h <= self.length:
            h = 10**h
            test_var.append(h)
        self.var = test_var

    def S_Sort(self):
        s = datetime.datetime.now()
        for h in self.var:
            for x in range(h):
                start = x
                i = 1
                while x+i*h < self.length:
                    for j in range(i-1,-1,-1):
                        if self.array[i*h+x] >= self.array[j*h+x]:
                            self.array = self.Insert(self.array, start, j+1, i, h)
                            break
                        else:
                            if j == 0: self.Insert(self.array, start,j, i, h)
                    i += 1
        print datetime.datetime.now() - s

        return self.array

    def InsertSort(self):
        s = datetime.datetime.now()
        for i in range(1, self.length):
            for j in range(i-1,-1,-1):
                if self.array[i] >= self.array[j]:
                    self.array.insert(j+1,self.array.pop(i))
                    break
                else:
                    if j == 0: self.array.insert(j,self.array.pop(i))
        print datetime.datetime.now() - s
        return self.array



    def Insert(self, array, start, compare, now, h):

        tmp = array[now*h+start]
        for x in range(now-1, compare-1, -1):
            array[(x+1)*h+start] = array[x*h+start]
        array[compare*h+start] = tmp
        return array






array = [5,4,3,2,1]
shell = Shell(array)
print shell.S_Sort()
print shell.InsertSort()



