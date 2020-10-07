tc=input("\nEnter the no. of test cases you want: ")

sletter=[]
for j in range((int(tc))):
    sletter.append(input("Enter a string: "))
for n in sletter:
    for i in range(len(n)):
        if i%2==0:
            print(n[i],end="")
    print(end=" ")
    for i in range(len(n)):
        if i%2!=0:
            print(n[i],end="")
    print("")