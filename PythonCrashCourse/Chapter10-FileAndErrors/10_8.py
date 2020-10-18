def print_file(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Sorry, we didn't want {filename}.")

print_file('cats.txt')
print_file('dogs.txt')