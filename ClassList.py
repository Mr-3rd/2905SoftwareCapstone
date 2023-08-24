"""
Lab1Q2 - Justin Third - 8/23/2023
Create a tool that creates and displays a classlist
    RESOURCES
    1 = In-class example built by Clara James
"""

Classes = []
classCount = 1

while True:
    className = input(f'Please enter class #{classCount} or press the ENTER key to exit: ')

    if className == "":
        break  # 1

    Classes.append(className)
    classCount = classCount + 1

print(f'Your class list:')
for item in Classes:
    print(f'Class: {item}')



