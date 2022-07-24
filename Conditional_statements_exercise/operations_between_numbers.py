number1 = int(input())
number2 = int(input())
operation = input()
even_or_odd = ''
total = 0
if operation == '+':
    total = number1 + number2
    if total % 2 == 0:
       even_or_odd = 'even'
    elif total % 2 != 0:
       even_or_odd = 'odd'
    print(f"{number1} {operation} {number2} = {total} - {even_or_odd}")
elif operation == '-':
    total = number1 - number2
    if total % 2 == 0:
        even_or_odd = 'even'
    elif total % 2 != 0:
        even_or_odd = 'odd'
    print(f"{number1} {operation} {number2} = {total} - {even_or_odd}")
elif operation == '*':
    total = number1 * number2
    if total % 2 == 0:
        even_or_odd = 'even'
    elif total % 2 != 0:
        even_or_odd = 'odd'
    print(f"{number1} {operation} {number2} = {total} - {even_or_odd}")
elif operation == '/':
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        total = number1 / number2
        print(f"{number1} {operation} {number2} = {total:.2f}")
elif operation == '%':
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        total = number1 % number2
        print(f"{number1} {operation} {number2} = {total}")


