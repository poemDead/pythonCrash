'''
加法运算 
提示用户提供数值输入时，常出现的一个问题是，
用户提 供的是文本而不是数。
在此情况下，当你尝试将输入转换为整数时，
将引发 ValueError 异常。
编写一个程序，提示用户输入两个数，再将其相加并打印结果。
在用户输入的任何一个值不是数时都捕获 ValueError 异常，
并打印一条友好的错误消息。
对你编写的 程序进行测试:先输入两个数，再输入一些文本而不是数。
'''
def plus():
    num1 = input('Enter first number:')
    num2 = input('Enter second number:')
    try:
        result = int(num1)+int(num2)
    except ValueError:
        print('Please enter a number not text.')
    else:
        print(f"{num1} + {num2} = {result}")

plus()