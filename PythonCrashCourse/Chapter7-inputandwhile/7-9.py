sandwich_orders = ['egg','fish','chicken','pastrami','pastrami','pastrami']
finished_sandwiches = []
print("Sorry, we are run out of pastrami today.")
while sandwich_orders:
    finished = sandwich_orders.pop()
    if finished == 'pastrami':
        continue
    print(f"i made your {finished.upper()}.")
    finished_sandwiches.append(finished)

print('\nThese sandwich orders are finished.')
for sand in finished_sandwiches:
    print(sand)