OPERATOR = ['+','-','*','/','%']
NUMBER = ['0','1','2','3','4','5','6','7','8','9']


class MStack(object):

    def __init__(self, expression):
        self.expression = expression
        self.exp = list(self.expression)

        self.numStack = []
        self.operatorStack = []

    def check(self):
        for x in self.exp:
            if x is ')':
                a = self.numStack.pop()
                b = self.numStack.pop()
                c = self.operatorStack.pop()
                tmp = '('+ str(b)+str(c)+str(a)+')'
                self.numStack.append(tmp)

            elif x in NUMBER:
                self.numStack.append(x)

            elif x in OPERATOR:
                self.operatorStack.append(x)

            elif x is '(':
                pass

            else:
                print ("error")

        last = self.numStack.pop()
        print last
        return last

m = MStack("1+2+3)*(4*5)))")
m.check()