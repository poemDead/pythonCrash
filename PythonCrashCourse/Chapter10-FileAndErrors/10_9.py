def print_file(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        pass

print_file('cats.txt')
print_file('../dogs.txt')