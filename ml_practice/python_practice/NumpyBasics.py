import numpy as np
# abc = np.array([[1,2,3,4],[1,2,3,4]])
# print(abc)

# a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# arr=np.array([1,2,3,4],ndmin=5)


# print(a)
# print(type(a))

# print(a.ndim)
# print(arr)
# print(arr.ndim)


# --------------arithmetic operations - ----------------------

a=np.array([[1,2,3],[1,2,3]])
b=np.array([[4,5,6],[4,5,6]])
c=np.add(a,b)
d=np.subtract(b,a)
e=np.multiply(a,b)
f=np.divide(b,a)
g=np.mod(b,a)
h=np.mean(a)
i=np.median(a)

print("a\n",a)
print()
print("b\n",b)
print("\n")
print("addition\n",c,"\n")
print("substraction B-A\n",d,"\n")
print("multiplication\n",e,"\n")
print("division B/A\n",f,"\n")
print("reminder B/A\n",g,"\n")
print("average of A:\n",h,"\n")
print("median of A:\n",i,"\n")



# ------------operations with every elements and all sum----------------------

# a=np.array([[1,2,3],[1,2,3]])
# b=np.array([[4,5,6],[4,5,6]])
# print("a\n",a)
# print()
# print("b\n",b)
# print("\n")
# print("addinga 4 to every elemet in A:\n",a+4)
# print("substracting 1 from every elemet in A:\n",a-1)
# print("sum of all array elements of A :\n",a.sum())




# --------- data type of arrayy elements --------------------

a=np.array([[1,2,3],[1,2,3]])
b=np.array([[4.9,5.8,6.4],[4.0,5.0,6.5]])
print()
print("data type of a:\n",a.dtype)
print()
print("data type of b:\n",b.dtype)

b=np.array([[4.9,5.8,6.4],[4.0,5.0,6.5]],dtype=np.int64)
print()
print("changing dtype of b to int:\n",b.dtype)
print()
print("B:\n",b)

# ---------------------math operation on dtypes array-----------------------


# a=np.array([[1,2,3],[1,2,3]],dtype=np.float64)
# b=np.array([[4.9,5.8,6.4],[4.0,5.0,6.5]])

# sum=np.add(a,b)
# print(sum)


# ----------------array slicing ---------------------

# array_2d=np.array([[5,4,4,7],[7,6,4,1],[1,4,3,7],[8,8,7,6]])
# print("Array:\n",array_2d)
# sliced_array=array_2d[:1,::2]
# print("Sliced Array:\n",sliced_array)
# print("sliced array dimensions:\n",sliced_array.ndim)


