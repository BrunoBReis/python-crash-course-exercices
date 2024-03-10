# List of messages

def show_messages(messages:list[str]):
    """Show messages of a list"""
    for message in messages:
        print(message)

def send_message(messages:list[str], sent_message:list[str]):
    """Passing messages to another list"""
    while messages:
        current_message = messages.pop()
        print(f'Sending message "{current_message}"')
        sent_message.append(current_message)



messages = ['hello, how are you', 'how you are doing?', 'hello!']
sent_messages = []

send_message(messages[:], sent_messages)
show_messages(sent_messages)
