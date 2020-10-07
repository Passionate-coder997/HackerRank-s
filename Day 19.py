#Python doesn't support Generics
#you can do it like this in java or C++ or
#any other Object Oriented language which supports Generics



class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor=[]
        for i in range(n):
            x = len([i for i in range(1,n+1) if n % i])
            divisor.append(x)
        res = sum(divisor)
        return res

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)