count = input("请问你们一共多少人用餐？")
count = int(count)

if count>8:
    print(f"{count}个人的话，我们现在没有空桌了，实在抱歉")
else:
    print(f"{count}个人还有空位，里面请")