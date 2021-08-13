"""

Array vs list

Array are the block of the contiguous memory elements of similar data types 
While list elements are scattered in different memory location and linked with reference for uniform sequence


"""

def Binary_search(lst:list, begin:list, last:list, element:int)->int:
    
    if begin > last:
        return -1
    else: 
        mid = (begin + last) // 2   
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            return Binary_search(lst, mid+1, last, element)
        elif lst[mid] > element:
            return Binary_search(lst, begin, mid-1, element)

input_list = list(range(100))
element_search = 0
flag = Binary_search(input_list, 0, len(input_list)-1, element_search)
print(f'item {element_search} found at index {flag} ') if flag != -1 else print('item not found ')