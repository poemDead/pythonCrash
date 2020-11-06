#!usr/bin/env python3

#coding:utf-8


import os

os.chdir(r'/Users/hanzhang/Downloads/123')

#os.listdir() 函数可以直接获取当前文件夹下所有可见文件的文件名

old_names = os.listdir(os.getcwd()) 

new_names = []

for i in range(30,40):
    new = "TPO" + str(i) + ".pdf"
    new_names.append(new)

new_names = list(map(lambda x: x.replace('.png', '.jpg'), old_names))


# 使用内置的 zip 方法一一对应地进行迭代

for old_name, new_name in zip(old_names, new_names):

	os.renames(old_name, new_name) #os.renames()方法直接替换文件名

print('文件已完成重命名……✅')