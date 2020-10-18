def plus():

    while True:
        num1 = input('Enter first number:')
        num2 = input('Enter second number:')
        if num1 == 'q':
            break
        if num2 == 'q':
            break
        try:
            result = int(num1)+int(num2)
        except ValueError:
            print('Please enter a number not text.')
        else:
            print(f"{num1} + {num2} = {result}")

plus()