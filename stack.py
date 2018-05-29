OPERATOR = ['+','-','*','/','%']
NUMBER = ['0','1','2','3','4','5','6','7','8','9']

class Stack(object):

    def __init__(self):
        self.input = []
        self.size = len(self.input)

    def enstack(self, ele):
        self.input.append(ele)
        self.size += 1
        return self.input

    def destack(self):
        self.size -= 1
        return self.input.pop()

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def size(self):
        return self.size

str = "(1+((2+3)*(4*5)))"
list = list(str)
ope = Stack()
num = Stack()

for x in list:
    if x in OPERATOR:
        print ope.enstack(x)
    elif x in NUMBER:
        print num.enstack(x)
    elif x is ')':
        tmp = ope.destack()
        if tmp == '*':
            num.enstack(int(num.destack()) * int(num.destack()))
        elif tmp == '/':
            num.enstack(int(num.destack()) / int(num.destack()))
        elif tmp == '+':
            num.enstack(int(num.destack()) + int(num.destack()))
        elif tmp == '-':
            num.enstack(int(num.destack()) - int(num.destack()))
        elif tmp == '%':
            num.enstack(int(num.destack()) % int(num.destack()))
print num.destack()






