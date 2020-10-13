nums = [value**3 for value in range(1,11)]

print(f"The first three items in the list are:{nums[:3]}.")
print(f"Three items from the middle of the list are:{nums[4:7]}.")
print(f"The last three items in the list are:”{[nums[-3:]]}.")

foods = ['steak','mcdonald','chickenbreast']
friend_foods = foods[:]

foods.append('protein')
friend_foods.append('luoshifen')

print("My favorite pizzas are:")
print(foods)
print(food for food in foods)