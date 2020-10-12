# int
2 + 3
# 5
3 - 2
# 1
2 * 3
# 6
3 / 2
# 1.5
3 ** 2
# 9
3 ** 3
# 27
10 ** 6
# 1000000
2 + 3*4
# 14
( 2 + 3 ) * 4
# 20

# float
0.1 + 0.1
# 0.2
0.2 + 0.2
# 0.4
2 * 0.1
# 0.2
# BUT!结果所包含的小数位数可能是不确定的
0.2 + 0.1
# 0.30000000000000004
3 * 0.1
# 0.30000000000000004
'''
所有语言都存在这种问题，没有什么可担心的。Python 会尽力找到一种精确表示结果的方法，
但鉴于计算机内部表示数的方式，这在有些情况下很难。就现在而言，暂时忽略多余的小数位数
即可。在第二部分的项目中，你将在需要时学习处理多余小数位的方式。
'''

# int & float
# 两数相除的结果总是浮点数，即使可以整除
4 / 2
# 2.0
# 另外，只要有浮点数存在，就肯定结果为浮点数

# 使用下划线让数字清晰易读
univere_age = 14_000_000_000
print(univere_age)
# 14000000000
# python 3.6以上才支持

# 同时给多个变量复制
x, y, z = 0, 1, 3

# 常量： python通常使用全大写来支持某个变量应该视为常量
MAX_CONNECTIONS = 5000