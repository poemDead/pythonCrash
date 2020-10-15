def sandwich(*toppings):
    if toppings:
        print('So you want your sandwich have these: ')
        for topping in toppings:
            print(topping)
        print('Ok, i got it.')
    else:
        print('So, you mean you want a bread not a sandwich?')

sandwich()
sandwich('tuna')
sandwich('egg','bacon')
    