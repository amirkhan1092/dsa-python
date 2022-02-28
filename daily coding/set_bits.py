'''
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''

N = 3
count = 0
for i in range(1, N+1):
    count += bin(i).count('1')
print(f'Total number of set bits upto {N} is {count}') 
