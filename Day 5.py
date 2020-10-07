num=int(input('Enter number to find its table:\n'))
for i in range(1,11):
	print(num,'*','{}'.format(i),'=',num*i)