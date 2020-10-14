# message = input('Tell me something and i will fudu it back to you:')
# print(message)

# prompt = "Tell me something and i will fudu it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message=""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)


prompt = "Tell me something and i will fudu it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"

active=True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)