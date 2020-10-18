'''
练习 10-3:访客 编写一个程序，提示用户输入名字。用户做出响应后，将其名
字写入文件 guest.txt 中。
'''

with open('guest.txt','w') as file:
    name = input('Give me your name: \n')
    file.write(name)
