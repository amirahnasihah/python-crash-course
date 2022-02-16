def show_messages(messages):
    """Series of short text messages"""   
    for message in messages:
        print(message)
    
    
# moves messages to send_messages.
def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    while messages:
        current_messages = messages.pop()
        print(f"The current messages {current_messages}")
        sent_messages.append(current_messages)
        
messages = ['Antonio Vivaldi is a great pianist.', 'Messi is GOAT.', 'hello there', 'how are u?', ':)']
sent_messages = []
show_messages(messages)