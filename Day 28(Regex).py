import re

N = int(input())
email=[]
for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]

    emailID = firstNameEmailID[1]

    x = re.findall("[a-z]+@(gmail)\.com$",emailID)
    if x:
        email.append(firstName)
for e in sorted(email):
    print(e)