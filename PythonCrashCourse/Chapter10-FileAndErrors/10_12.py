import json

def get_num():  
    num = input('Give me your favorite number: ')

    with open('fav_num_1.json','w') as f:
        json.dump(num,f)    

def read_num():
    with open('fav_num_1.json') as f:
        fav_num = json.load(f)
    return fav_num

def get_show_num():
    try:
        fav_num = read_num()
    except FileNotFoundError:
        get_num()
    else:
        print(f"I know your favorite number! It’s {fav_num}.")

get_show_num()
