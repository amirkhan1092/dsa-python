"""This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, 
return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, 
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3."""


def max_profit(stock_prices:list, k:int)->int:
    inc = 0
    exc = 0
    for i in stock_prices:
        inc = inc if inc > exc else exc
        exc = inc + i


        


arr = eval(input('stock prices '))
buy = int(input('enter the number of exchange buy '))
out_profit = max_profit(arr, buy)
print(out_profit)