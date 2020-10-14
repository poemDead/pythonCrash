message = "请您输入想要添加的披萨配料：\n"
message += "输入“退出”，结束添加。\n"

while True:
    topping = input(message)

    if topping == '退出':
        break
    
    print(f"好的，我们会在披萨中添加 {topping}。")
