names = ["hannai","sanxing","yangyeah","zhushui"]
for i in range(len(names)):
    message = f"What's up, {names[i]}"
    print(message)

# 修改列表
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)

# 添加元素
# append()
motocycles.append('honda')
print(motocycles)

motos = []
motos.append('honda')
motos.append('suzuki')
motos.append('yamaha')
print(motos)
# insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) 

# 删除元素
# del
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)
# pop()
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
poped_moto = motocycles.pop()
print(poped_moto)
print(motocycles)
# 指定位置弹出
motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
first_owned = motocycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}.") 
print(f"The first motorcycle I owned was a {first_owned.title()}.") 
# remove()根据值删除元素
motocycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles)
motocycles.remove('ducati')
print(motocycles)