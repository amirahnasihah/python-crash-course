# start from exercise 8-10.

def show_messages(messages):
	"""Print all messages in the list."""
	print("This messages in list.")
	for message in messages:
		print(message)
		
def send_messages(messages, sent_messages):
	"""Print each message, and then move it to sent_messages."""
	print("\nWant to move to sent_messages list using while.")
	while messages:
		current_messages = messages.pop()
		print(current_messages)
		sent_messages.append(current_messages)
		
messages = ['kyuhyun', 'at gwanghwamun', '1', 'this', 'is', 'list']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists: ")
print(messages)
print(sent_messages)
