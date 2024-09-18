# Arden
# 9/18/24
# Numbers Practice

from colorama import Fore # Everything that starts with Fore is for coloring the text so it looks nice :)

num1 = float(input('Enter a number: '))
operation = input(f"Enter your Operation \n{Fore.RED}ONLY{Fore.RESET} type '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division. \n")
num2 = float(input('Enter another number: '))

while True: # The while loop is so you don't have to re-enter your numbers if you mess up the operation
    if operation == '+':
        total = num1 + num2
        break
    elif operation == '-':
        total = num1 - num2
        break
    elif operation == '*':
        total = num1 * num2
        break
    elif operation == '/':
        total = num1 / num2
        break
    else:
        print(Fore.RED + '\nInvalid opperation please try again. \n' + Fore.RESET)
        operation = input(Fore.GREEN + "Renter your Operation \nType '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division. No spaces of \n" + Fore.RESET)

total_find = str(total).find('.')
offset = int(total_find) + 3

print('Your total is ' + Fore.GREEN + str(total)[0:offset] + Fore.RESET)
