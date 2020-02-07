num=int(input("Enter number"))
list = []
n=int(input("Enter n"))
for i in range(n):
	no=int(input())
	list.append(no)
flag=0
for i in range(len(list)):
	if(list[i]==num):
		flag=1
		break

if flag==1:
	print("Element Exist")
else:
	print("Element Not found")

	
	
