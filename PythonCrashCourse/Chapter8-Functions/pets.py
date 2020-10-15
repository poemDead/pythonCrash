# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster','harry')
# describe_pet('dog','whillie')

# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type = 'hamster',pet_name = 'harry')
# describe_pet('dog','whillie')

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster',pet_name = 'harry')
describe_pet(pet_name='whillie')