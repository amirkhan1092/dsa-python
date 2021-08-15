"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

def Rooms_required(list_intervals:list)->int:
    pass
    test_number = 10000
    array_test = [0] * test_number
    for i, j in list_intervals:
        array_test[i] += 1
        array_test[j] += -1
    rooms, temp = 0, 0
    for i in array_test:
        temp += i
        if temp > rooms:
            rooms = temp
    return rooms

# def solution(n):
#      time_counter = [0 for i in range(1441)]
#      for i in n:
#          time_counter[i[0]] += 1
#          time_counter[i[1]] += -1
#      rooms, tmp = 0, 0
#      for i in time_counter:
#          tmp += i
#          if(tmp > rooms):
#              rooms = tmp
#      return rooms


# intervals = eval(input())
intervals = [(30, 75), (0, 50), (60, 150)]
out = Rooms_required(intervals)
# out = solution(intervals)
print(f"Number of the Rooms required {out}")
