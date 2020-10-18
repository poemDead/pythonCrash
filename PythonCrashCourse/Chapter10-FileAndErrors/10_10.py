def count_words():
    filename = input('Please enter your filename:')
    word = input('Please enter the word you want to count:')
    try:
        with open(filename) as f:
            text = f.read()
        count = text.lower().count(word)
    except FileNotFoundError:
        pass
    else:
        print(f"There are {count} '{word}' in {filename}.")

count_words()