Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=int(input("Enter size of list:"))

list1=[int(ele) for ele in input("Enter list element:").split()]
list1.sort()
max=list1[-1]
for i in range(max):
    if((i+1) not in list1):
        print("missing number is :",i+1)    
        exit()
print("Missing first natural number is :",max+1)