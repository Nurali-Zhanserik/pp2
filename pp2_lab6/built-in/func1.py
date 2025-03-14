from functools import reduce
size = int(input("Enter a size:"))
mylist = []
for i in range(size):
    a = int(input("enter a element:"))
    mylist.append(a)
result = reduce(lambda x,y: x*y, mylist)
print(result)    


