# 检查两个字符串相等和不等。
print("subaru"=='subaru')
print('subaru'=='mazuda')
print("subaru"!='sUbaru')
print('abc'!='abc')
# 使用方法 lower()的测试。
print('subaru'=='Subaru'.lower())
print('subada'=='Subaru'.lower())
# 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。
print(1==1)
print(1==2)
print(2!=1)
print(2!=2)
print(3>2)
print(5>6)
print(2<7)
print(6<2)
print(1>=1)
print(2>=5)
print(1<=3)
print(7<=2)
# 使用关键字 and 和 or 的测试。
print("subaru"=='subaru' and "subaru"!='sUbaru')
print("subaru"=='subaru' and 'abc'!='abc')
print('subaru'=='mazuda' or "subaru"!='sUbaru')
print(1==2 or 'abc'!='abc')
# 测试特定的值是否包含在列表中。
banned_users = ['andrew', 'carolina', 'david'] 
print('andrew' in banned_users)
# 测试特定的值是否未包含在列表中。
print("andrew" not in banned_users)