"""
Exercise: Array DataStructure
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
"""

list_expenses = [('January', 2200), ('February', 2350), ('March', 2600), ('April', 2130), ('May', 2190)]
hash_table = dict(list_expenses)

# find out 1
spent_extra = hash_table['February'] - hash_table['January']
print(f"Extra amount spent in Feb compare to Jan {spent_extra}$")

# find out 2
quarter_expense = sum([v for i, v in list_expenses[:3]])
print(f"Total Expenses in fist quarter {quarter_expense}$")


