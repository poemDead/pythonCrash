'''
练习 10-4:访客名单 编写一个 while 循环，提示用户输入名字。
用户输入名字 后，在屏幕上打印一句问候语，并将一条到访记录添加到文件
 guest_book.txt 中。确保 这个文件中的每条记录都独占一行。
'''

with open('guset_book.txt','a') as file:
    name = input('Please enter your name\n')
    file.write(f"{name}\n")
    print(f"Hello,{name}!")