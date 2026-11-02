def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = [
    "Hello, how are you?",
    "Keep learning Python!",
    "Practice makes perfect."
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nMessages:")
print(messages)

print("\nSent Messages:")
print(sent_messages)