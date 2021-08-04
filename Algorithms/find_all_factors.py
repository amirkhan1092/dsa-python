"""
Algorithm 

Step 1: cosider the positive Number value for the factors
Step 2: initialize the counter = 1
Step 3: Display the value of counter if Counter is divisor of Value
Step 4: Increment in Value of counter and if count < Number goto the Step 3  

"""



def All_factors(num:int)->int:
    """All positive of positive Integer Quantity """
    count = 1
    out = []
    while count <= num:
        if num % count == 0:
            out.append(count)
        count += 1
    return out

N = 15
print(All_factors(N))