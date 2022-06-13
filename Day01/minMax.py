#Link: https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
a = [3,2,1,56,1000,167]
minni = a[0]
maxi = a[-1]
print(minni, maxi)
for i in a:
    if i<minni:
        minni = i
    if i>maxi:
        maxi = i
print(minni, maxi)

# min(a) and max(a) can also be used