
# nptell week 3 Assignment 

"""
Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute 
difference between each adjacent pair of elements strictly increases.

>>> expanding([1,3,7,2,9])
  True
"""

def expanding(l:list)->bool:
    
    if len(l) <= 2:
        return True 
    else:
        ele1 = l[0]
        ele2 = l[1]
        diff = abs(ele1 - ele2)
        print(diff)
        return diff < (abs(l[1] - l[2])) and expanding(l[1:])     
input()
input_list = list(map(int, input().split()))  # [1, 3, 7, 2, -6]

out = expanding(input_list)
print(f"{out}")