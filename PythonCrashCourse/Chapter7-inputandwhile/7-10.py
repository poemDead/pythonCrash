responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name?')
    response = input('If you could visit one place in the world, where would you go?')

    responses[name] = response

    repeat = input('Another person want to respond?(Yes/No)')
    if repeat.lower() == "no":
        polling_active = False

print("\n------------Poll Results-------------")
for n,r in responses.items():
    print(f"{n.title()} would visit {r} someday.")