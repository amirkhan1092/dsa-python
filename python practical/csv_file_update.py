"""
create a csv file by entering user-id and password, read and search the password for given user-id 

"""

import pandas as pd

data = []
flag = 'Y'
while flag != 'N':
    user_id = input("Enter the user-id: ")
    password = input("Enter the password: ")
    data.append([user_id, password])
    flag = input("Do you want to enter another entry Y/N: ").strip()



df = pd.DataFrame(data, columns=["user-d", "password"])
print(df)
df.to_csv('e:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\password.csv')