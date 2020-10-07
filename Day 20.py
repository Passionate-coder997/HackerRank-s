n=int(input())
numSwaps=0
a=list(map(int, input().strip().split()))

for i in range(n-1):
    for j in range(n-i-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            numSwaps+=1

print(f"Array is Sorted in {numSwaps} swaps")
print(f"First Element: {a[j]}")
print(f"Last Element: {a[j-1]}")