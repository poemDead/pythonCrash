import json

def get_num():  
    num = input('Give me your favorite number: ')

    with open('fav_num.json','w') as f:
        json.dump(num,f)    

def show_num():
    with open('fav_num.json') as f:
        fav_num = json.load(f)
    print(f"I know your favorite number! It’s {fav_num}.")

get_num()
show_num()