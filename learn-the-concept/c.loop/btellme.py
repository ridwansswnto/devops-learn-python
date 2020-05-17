prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit' and message != 'exit':
    message = input(prompt)

    if message != 'quit' and message != 'exit':
        print(message)