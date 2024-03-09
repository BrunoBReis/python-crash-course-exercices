# List of messages

def send_messages(message:str, sent_message:list):
    sent_message.append(message)
    print(f'This message "{message}" was sent')

def show_messages(list_messages:list[str]):
    """Printing message list"""
    sent_messages = []
    for message in list_messages:
        send_messages(message, sent_messages)
    return sent_messages

    


messages = ['hello, how are you', 'how you are doing?', 'hello!']

new_list = show_messages(messages[:])

print(new_list)