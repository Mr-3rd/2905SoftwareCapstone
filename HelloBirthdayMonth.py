"""
Lab1Q1 - Justin Third - 8/23/2023
first project, both my pycharm, python, and git melted down in class. I'm quite lucky I even built this one
I realize I capital cased my variables, I will use camel case going forward

    References:
    1 = https://automatetheboringstuff.com/2e/chapter8/
    2 = https://www.askpython.com/python/examples/obtain-current-year-and-month#:~:text=In%20Python%2C%20you%20can%20obtain,function%20to%20format%20the%20output.
"""

import pyinputplus as pyip
from datetime import datetime

UserName = input("Please enter your preferred name: ")

NameLength = len(UserName.replace(" ", ""))

UserMonth = pyip.inputNum("Please enter the month of your birth (Number of Month Accepted): ")  # 1

while int(UserMonth) < 1 or int(UserMonth) > 12:
    UserMonth = input("Please enter the month between 1 and 12 (Number of Month Accepted): ")

print(f'Initializing User: {UserName}!')
print(f'Letter count of User Name: {NameLength}')
ThisMonth = datetime.now().month  # 2

if ThisMonth == UserMonth:
    print(f'{UserName}, it is your birthday month: {UserMonth}')
else:
    print(f'{UserName}, It is not your birthday month. Birth: {UserMonth} VS Current: {ThisMonth}')
