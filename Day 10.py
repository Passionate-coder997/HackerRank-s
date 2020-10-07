'''def slice(num):
    return num[2:]

n=int(input())
a=max(slice(bin(n)).split('0')).count('1')
print(a)'''

print(sorted(list(map(len,'{0:b}'.format(int(input().strip())).split("0"))),reverse=True)[0])