'''
练习 10-5:调查 编写一个 while 循环，询问用户为何喜欢编程。每当用户输入
一个原因后，都将其添加到一个存储所有原因的文件中。
'''
with open('reasons.txt','a') as file:
    reason = input('Please enter why you alove programming\n')
    file.write(f"{reason}\n")