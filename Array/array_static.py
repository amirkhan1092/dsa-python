"""
Python list is type of the dynamic array 
where location of the contiguous bytes change in group of the insertions 
"""


# big O notation with array 
# search the record by index and calculate the value  O(1)
'''here the size of the array not effect the time growth with input'''
lst = ['sakib', 'razia', 'sultan', 'mehboob']
greeting = 'Good Morning'
ind = int(input('enter the index of the name '))
print(greeting, lst[0])



# search by value O(n)
# find the maximum value in an array 

# user input array
arr = [1, 2, 4, 54, 22, 43, 23, 33, 54]

mx = arr[0]

for i in arr:
    mx = mx if i <= mx else i

print(f'the maximum value in the array is {mx}')



#  search the any elements O(n)
arr = [1, 2, 4, 54, 22, 43, 23, 33, 54]
ele = eval(input('enter the element for the searching '))

for i in arr:
    if ele == i:
        print(f'item {ele} found')
        break

print(f'item {ele} not found ')



# search the element with O(log(n))
# binary search always work on sorted array 
arr = [1, 2, 4, 22, 23, 33, 43, 54]
# ele = eval(input('enter the element for the searching '))
ele = 2
ln = len(arr)
start = 0
end = ln - 1
mid = (start + end)//2

for i in range(ln):
    mid = (start + end)//2
    if arr[mid] == ele:
        print(f'elment {ele} found')
        break
    elif arr[mid] < ele:
        start = mid + 1
    elif arr[mid] > ele:
        end = mid - 1
    elif start >= end:
        print(f'item {ele} not found ')
        break

else:
    print('loop completed!')





