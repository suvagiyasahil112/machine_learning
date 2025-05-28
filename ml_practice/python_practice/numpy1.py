import numpy as np
import random 

# ab = np.arange(1,11)
# print(ab)



# abc = np.random.randint(1,10)
# print("hh",abc)
# arry1d = np.array([1,2,3])
# mul = arry1d *2
# print("array1",arry1d)

# arr2d = np.array([[1,2,3],[1,2,3]])
# arr2d(3,2)
# # arr2d[0,1]=0
# print("array2",arr2d)

# arr3d = np.array([[1,2,3],[4,5,6],[1,2,3]])
# print("array3",arr3d)

# n1 = np.random.randint(1,11)

# print("task1")


aa=np.random.default_rng()
arr1 = aa.integers(9 , size=9)
aar11 = np.array(arr1,ndmin=2)
print("array 1:\n",aar11)
bb=np.random.default_rng()
arr2 = bb.integers(9 , size=9)
aar22 = np.array(arr2,ndmin=2)
# print("array 2:\n",aar22)
  
a=np.reshape(aar11,(3,3))
b=np.reshape(aar22,(3,3)) 

print("A:\n",a)
print("B:\n",b)
# print("addition of array 1 and array 2:\n",a+b)
 
# print("substraction  of array2 and array 1:\n",a-b)

# print("multiplication of array 1 and array 2:\n",a*b)

# print("division of array 1 and array 2:\n",aar11/aar22)

# -----------------------replacing element------------------------------


# print("A before replacement\n",a)

# print("element to be replaced from A :",a[1][1])
# a[1][1]=0

# print("A affter replacement\n",a)


# -----------------------dot product of A.B--------------------------------
# print()
# print("Dot Product of A,B :\n",np.dot(a,b),"\n")


# print("Dot Product of B,A :\n",np.dot(b,a))


# aa = np.random.randint(1,10,size=30,)
# print(aa)

# -----------------------5*5--------------------------------


# arange=np.random.default_rng()
# a1d=arange.integers(10,50,25)

# # print("A one dimensional:\n",a1d)
# a=np.reshape(a1d,(5,5))

# print("A:\n",a)


# first_row=a[0]
# print("\n")
# print("First row:\n",first_row)
# print("\n")

# last_col=a[:,4]
# print("last column:\n",last_col)
# print("\n")

# center_metrix=a[1:-1,[1,2,3]]
# print("center metrix:\n",center_metrix)


