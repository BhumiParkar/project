"""n=int(input("Enter the number of elements:"))
arr=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
sum=0
for i in arr:
    sum=sum+i

print("Sum of array elements= ",sum)
 

#Addition of two arrays
n=int(input("Enter the number elements:"))
arr1=[]
arr2=[]
result=[]
print("ENter the elements of the first array:")
for i in range(n):
    arr1.append(int(input()))
print("Enter the elements of the second array:")
for i in range(n):
    arr2.append(int(input()))
for i in range(n):
    result.append(arr1[i]+arr2[i])
print("First array:",arr1)
print("Second arrayt:",arr2)
print("Sum array:",result)
"""

#Matrix creation
m1=[]
r1=int(input("Enter number of rows for matrix 1:"))
c1=int(input("Enter the number of columns for matrix 1:"))
for i in range(0,r1):
    a=[]
    for j in range(0,c1):
        a.append(int(input("Enter data for m1")))
        m1.append(a)
print(m1)
