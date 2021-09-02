"""
the power function with min value of iteration 


"""


def pow(x:int, y:int)->int:
    # s = 1
    # for i in range(y):
    #     s *= x
    # return s
    # if y == 0: return 1
    # elif x == 0: return 0
    # else:
    #     return x * pow(x, y - 1)
        
    # if y == 0:
    #     return 1
    # elif y % 2 == 0:
    #     return pow(x, y // 2) * pow(x, y // 2)
    # else:
    #     return x * pow()

    temp = 0
    if y == 0:
        return 1

    temp = pow(x, y//2)
    if y % 2 == 0:
        return temp * temp

    else:
        return x * temp * temp 


a = 2
b = 5
res = pow(a, b)
print(f"The result of a to the power of b is {res}")