import numpy as np
import random

# print("\nzeroes array:")
# zeros_array= np.zeros((3,3))
# print(zeros_array)
# print("\nones array:")
# ones_array=np.ones((2,2))
# print(ones_array)   
# print("\nidentity matrix:")
# identity_matrics= np.eye(5)
# print(identity_matrics)
# print()

# arr=np.array([1,2,3,4,5])

# powers=np.power(arr,3)

# print("3 power of arr :\n",powers)

# exponentials=np.exp(arr)
# print("exponential of array:\n",exponentials)

# ------------------------------sine cosine------------------------------


# arr=np.array([1,2,3,4,5])
# arr1=np.array([1,2,3,4,5])

# s = np.split(2,3)
# print(s)


# sine_value=np.sin(arr*np.pi/180)
# cosine_value=np.cos(arr*np.pi/180)

# print("Array:\n",arr)
# print("Sine:\n",sine_value)
# print("cosine value:\n",cosine_value)



# ------------------------------linear equations------------------------------ 


# CONSIDER the system : 3x + 4y =5 and 2x-y=1

# coefficients = np.array([[3,4],[2,-1]])
# constants = np.array([5,1])

# sol=np.linalg.solve(coefficients, constants)

# print("solution :", sol)



# ---------------------------stake-------------------------------------


# dstake depth wise 
# arr1=np.array([1,2,3,4,5,6,7,8,9,10])
# arr2=np.array([11,12,13,14,15,16,17,18,19,20])

# dstake=np.dstack([arr1,arr2])
# print("after dstake:\n",dstake)

#  vstack 


# arr1=np.array([1,2,3])
# arr2=np.array([11,12,13])


# vstake=np.vstack((arr1,arr2 ))

# print(" after vstake:\n",vstake)


# hstake


# arr1=np.array([[1],[3]])
# arr2=np.array([[11],[13]])

# hstake=np.hstack((arr1,arr2))   
# print("after h stake :\n",hstake)



# -------------------------splits---------------------------------------

# arr=np.array([1,2,3,4,5,6])

# arr_split=np.split(arr,3)
# print("split into 3 equal parts:",arr_split)


#  use indices to specify un even splits

# arr_split=np.split(arr,[5])

# print("split by indices:\n",arr_split)




# hsplit functon horizontal axis

# arr=np.array([1,2,3,4,5,6])

# print("array:",arr)

# hsplit=np.split(arr,2)  #split into 3 columns

# print("hsplit:",hsplit)

# vsplit
# arr=np.array([[[0,  1],[2,  3]],[[4,  5],[6,  7]]])
# print("Array before split:\n",arr)
# vsplit=np.vsplit(arr,2)
# print("vsplit:n",vsplit)


