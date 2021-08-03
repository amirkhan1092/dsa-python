"""
1. Suppose d devides both m and n, where m > n
2. Then m = ad, n = bd
3. So m - n = ad - bd => (a-b)d
4. d divides m-n as well!
5. so gcd(m, n) == gcd(n, m-n)

final
1. cosider gcd(m, n) with m > n
2. if n divides m return n
3. otherwise compute gcd(n, m-n) and return that value



"""

def gcd(m:int, n:int)->int:
    "consider m > n"
    if not m > n:
        m, n = n, m
        # return gcd(m, n)
    if m % n == 0:
        return n
    else:
        return gcd(m-n, n)    


num1 = 16
num2 = 8
out = gcd(num1, num2)
print(out)