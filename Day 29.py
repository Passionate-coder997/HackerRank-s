#Objective:
#Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!
#Task:
#Given set S={1,2,3,....N}. Find two integers,A and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

#!/bin/python3

def find_max(n, k):
    max = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bitand = i & j
            if max < bitand < k:
                max = bitand
                if max==k-1:
                    return max
    return max

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(find_max(n, k))