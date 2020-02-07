list1=[1,2,3,4,5]
list2=[10,6,7,8,9]

flag=0
for x in list1:
	for y in list2:
		if x==y:
			flag=1
			break
if flag==1:
	print("Common Element Exist")

else:
	print("No common element Exist")			
