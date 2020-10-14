responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name?')
    response = input('Which mountain would you like to climb someday?')

    responses[name] = response

    repeat = input('Another person want to respond?(Yes/No)')
    if repeat.lower() == "no":
        polling_active = False

print("\n------------Poll Results-------------")
for n,r in responses.items():
    print(f"{n.title()} would like to climb {r} someday.")