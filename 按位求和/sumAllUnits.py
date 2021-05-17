class sumAll :
    def __init__(self,intN):
        self.value = intN
        self.sum = self.sumAllUnit(intN)

    def sumAllUnit(self,intN):
        if intN < 10:
            return intN
        else :
            last = intN % 10
            intN //= 10
            return last + self.sumAllUnit(intN)

num = sumAll(87)
print(num.sum)