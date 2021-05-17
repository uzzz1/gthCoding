#方法一
class sumAll :
    def __init__(self,intN):
        self.value = intN
        self.sum = self.sumAllUnit(intN)
        self.sumTillBot = self.sumBot(intN)

    def sumAllUnit(self,intN):
        if intN < 10:
            return intN
        else :
            last = intN % 10
            intN //= 10
            return last + self.sumAllUnit(intN)
    
    def sumBot(self,intN):
        if intN < 10:
            return intN
        else :
            intN = self.sumAllUnit(intN)
            return self.sumBot(intN)

num = sumAll(77662)
print(num.sum)

#方法二：
class solution:
    def __init__(self,intN):
        self.sum = sum(list(map(int,str(intN))))
num = solution(77662)
print(num.sum)