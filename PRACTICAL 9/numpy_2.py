import numpy as np

arr = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


print("Dimension of arr :",arr.ndim)
print("Dimension of arr_2d :",arr_2d.ndim)
print("Dimension of arr_3d :",arr_3d.ndim)
print("--------------------------------")


arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

arr_sum = arr_1 + arr_2
arr_diff = arr_2 - arr_1
arr_product = arr_1 * arr_2

print("Sum of two arr : ",arr_sum)
print("Difference of two arr : ",arr_diff)
print("Product of two arr : ",arr_product)
print("--------------------------------")

# reshaping arrays
arr1 = np.arange(12)
new_arr = arr1.reshape(2,2,3)
print(" arr before reshaping : \n",arr1)
print(" arr after reshaping : \n",new_arr)
print("--------------------------------")