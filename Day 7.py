n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().split(' ')]

for i in range(len(arr)):
    print(str(arr[-i-1]), end=" ")
