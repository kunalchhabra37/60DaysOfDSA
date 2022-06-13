# Link: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
arr = [1,1,0,2,2,2,1,0,0,1,2,0,1]
a = {}
for i in arr:
    try:
        a[i] += 1
    except:
        a[i] = 1
b = [0]*a[0] + [1]*a[1] + [2]*a[2]
print(b)