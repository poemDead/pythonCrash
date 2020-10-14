message = "请告诉我您的年龄：\n"

while True:
    age = input(message)
    age = int(age)

    if age < 3:
        print(f"婴儿免费，请进。")
        break
    elif age > 12:
        print(f"全票，15美元，请付款。")
        break
    else:
        print(f"小朋友打折，10美元即可，请付款")
        break
