"""
Quicksort is a divide-and-conquer algorithm. 
It works by selecting a 'pivot' element 
from the array and partitioning the other elements into two sub-arrays

"""

def quick_sort(A:list, l:int, r:int)->None:
    if r - l <= 1:  # Base case 
        return None

    # A[l] the pivot element
    yellow = l+1
      
    for green in range(l+1, r):
        if A[green] <= A[l]:
            A[yellow], A[green] = A[green], A[yellow]
            yellow = yellow +1

    # move pivot into the place 
    A[l], A[yellow-1] = A[yellow-1], A[l]

    quick_sort(A, l, yellow-1)
    quick_sort(A, yellow, r)




arr = [2, 4, 6, 12, 0, 45]
res = quick_sort(arr, 0, len(arr))
print(f"Sorted data after Applying Quicksort\n{arr} and return {res}")

