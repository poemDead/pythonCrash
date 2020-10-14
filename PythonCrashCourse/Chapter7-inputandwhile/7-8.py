sandwich_orders = ['egg sand','fish sand','chicken sand']
finished_sandwiches = []

while sandwich_orders:
    finished = sandwich_orders.pop()
    print(f"i made your {finished.upper()}.")
    finished_sandwiches.append(finished)

print('\nThese sandwich orders are finished.')
for sand in finished_sandwiches:
    print(sand)