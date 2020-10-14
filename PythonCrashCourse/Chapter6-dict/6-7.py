peoples = {
    'hannai':{
        'first_name':'nai',
        'last_name':'han',
        'age':'25',
        'city':'xian'
    },
    'ab':{
        'first_name':'ab',
        'last_name':'zhai',
        'age':'25',
        'city':'tokyo'
    },
    'yeah':{
        'first_name':'yeah',
        'last_name':'yang',
        'age':'25',
        'city':'newyork'
    }
}

for n,v in peoples.items():
    print(f"nick_name:{n}")
    first_name = v['first_name']
    last_name = v['last_name']
    age = v['age']
    city = v['city']

    print(f"\tFirst Name:{first_name}")
    print(f"\tLast Name:{last_name}")
    print(f"\tAge:{age}")
    print(f"\tCity:{city}")