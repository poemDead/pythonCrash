num = input("告诉我一个数，我看看是不是10的整数倍")
num = int(num)

if num % 10 == 0:
    print(f"{num}是10的整数倍")
else:
    print(f"{num}不是10的整数倍")