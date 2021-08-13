"""
selection sort, sort the array by repeatidly findling the mininmum element in the array  

"""


def selection_sort(A:list)->list:
    for i in range(len(A)):
        min_element = i
        for k in range(i+1, len(A)):
            if A[min_element] > A[k]:
                min_element = k
        A[i] , A[min_element] = A[min_element], A[i]    


lst_input = [2, 8, 4, 0, 1]
selection_sort(lst_input)
print(lst_input)
