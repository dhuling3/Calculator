#UI 

print(' Welcome To Calculator! To begin, select a choice between 1/2/3/4')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = int(input('What number ? :'))

if choice in [1,2,3,4]:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == 1:
        print(f'The result of addition is: {num1 + num2}')

    elif choice == 2:
        print(f'The result of subtraction is: {num1 - num2}')

    elif choice == 3:
        print(f'The result of multiplication is: {num1 * num2}')
        
