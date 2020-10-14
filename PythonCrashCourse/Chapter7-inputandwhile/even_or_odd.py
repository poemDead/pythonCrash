number = input("给我一个整数，我告诉你是奇数还是偶数。")
number = int(number)

if number % 2 == 0:
    print(f"\n{number}是个偶数。")
else:
    print(f"\n{number}是个奇数。")