# Lists are Mutable
from numpy import array2string


arr = [1,2,"Hello", [1,3], True]
arr2 = arr #Same as arr, so change in arr will also change arr2
arr3 = [1,2,"Hello", [1,3], True] #Value is same as arr but it is not arr, hence chamge in arr won't change arr3
print(arr2 is arr)
print(arr == arr3)
print(arr is arr3)

#List Slicing
print(arr[1:4]) #It returns a List

#List Concatenation
print(arr + [3,5,6])
arr6 = [y for x in [arr, [2,3,4]] for y in x]
print(arr6)

#List Copy
arr4 = arr.copy() #It creates a new copy of the list
arr5 = arr[:] #It is eqivalent to arr[0:len(arr)] which also return new copy of list
print(arr4)
print(arr4 == arr)
print(arr4 is arr)

#Lists are mutables
arr[2] = "World"
print(arr)

#List Comprehension 
arr7 = [x for x in range(10) if x%2==0]
print(arr7)

def lchange(arr):
    for i in range(len(arr)):
        arr[i] = 0
lchange(arr)
print(arr)