class Calculator:
    def power(self,n,p):
        try:
            res = pow(n, p)
            if n<0:
                e=ValueError("n and p should be non-negative")
                raise e
            elif p<0:
                e = ValueError("n and p should be non-negative")
                raise e
        except Exception as e:
            res = "n and p should be non-negative"
        return res


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)