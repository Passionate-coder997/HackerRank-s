try:
    num=input("Enter String to be converted to integer")
    int_num=int(num)
    print(int_num)
except ValueError:
    print("Bad String")