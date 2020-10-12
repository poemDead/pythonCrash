guest_names = ['Tom','Bob','Alice']
for i in range(len(guest_names)):
    print(f"请今晚来和我共进晚餐吧，{guest_names[i]}！")

cannot_come = 'Tom'
print(f"我才知道，{cannot_come}今天晚上不能来了。真是遗憾")

guest_names[0] = 'Emily'
for i in range(len(guest_names)):
    print(f"请今晚来和我共进晚餐吧，{guest_names[i]}！")

print("定了个包间，再邀请几个人吧！")
guest_names.insert(0,'DavId')
guest_names.insert(2,'maria')
guest_names.append('JimmY')
for i in range(len(guest_names)):
    print(f"请今晚来和我共进晚餐吧，{guest_names[i].title()}！")

print("哦不，还是只能来两个人了")
for i in range(len(guest_names)-2):
    poped = guest_names.pop()
    print(f"真是抱歉{poped}，我们还是改天再约吧。")

for i in range(len(guest_names)):
    print(f"请今晚来和我共进晚餐吧，{guest_names[i]}！")

for i in range(len(guest_names)):
    del guest_names[0]

print(guest_names)