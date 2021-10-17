'''
This problem was asked by Google.
Given an array of elements, return the length of the longest subarray 
where all its elements are distinct.
For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
subarray of distinct elements is [5, 2, 3, 4, 1]
'''
def unique(arr: list ):
    return len(set(arr)) == len(arr)

lst = eval(input("Enter the list elements "))
ln = len(lst)
mx = []
for i in range(ln):
    for j in range(i, ln):
        tp = lst[i:j+1]
        if unique(tp):
            mx = tp if len(tp) > len(mx) else mx
print(mx, len(mx))            





