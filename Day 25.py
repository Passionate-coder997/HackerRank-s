import math
def isPrime(n):
    if n<2:
        return False
    i = 2
    limit = math.sqrt(n)
    while i<limit:
        if n % i ==0:
            return False
        i+=1
    return True

T = int(input())
for i in range(T):
    n=int(input())
    res = isPrime(n)
    if res:
        print('Prime')
    else:
        print('Not Prime')













'''def isPrime(n):
    for i in range(2,n):
        if n % 2 == 0:
            return 'Not Prime'
    return 'Prime'
if __name__=='__main__':
    T=int(input())

    for i in range(T):
        n = int(input())
        print(isPrime(n))
'''

'''
index = 2
    if(index<=n-1):
        if(n%index==0):
            print('Not Prime')
        index+=1
        if(n%index!=0):
            print('Prime')
'''