import json


MESSAGE_FILE_PATH = 'data/messages.json'

# Calling the Json with our messages.
def get_all_messages():
    with open('data/messages.json', 'r') as f:
        messages = json.load(f)
        return messages
    '''Get a list of all the messages, loaded from the json file.'''


def save_messages(messages):
    with open('data/messages.json', 'w') as f:
        compose.dump([form, subject, body,])


    '''Save the given messages (list) to the json file.'''
    

# vi skappar en ny list sedan har vi en annan lista med messages som har hela json filen i sig.
# Vi skappar en for loop kollar igenom varje meddelande om den passar med username som är inloggad så kommer den
# göra en append till den nya listan. 
def get_messages(username):
    messages_to_user = []
    messages = get_all_messages()
    for message in messages:
        if message['to'] == username:
            messages_to_user.append(message)
    return messages_to_user
    '''Get a list of all messages which are addressed to the given user.'''


# None är om vi inte hittar några emails. 
# Vi loopar igenom kollar om vi hittar email som passar till ID.
def get_message(id):
    found_email = None
    emails = get_all_messages()
    for email in emails:
        if id == email['id']:
            found_email = email
            break
    return found_email
    '''Get the message with the given id.
    Return it if found, otherwise return None.'''


def get_max_id(messages):
    max_id = 0
    for message in messages:
        if message['id'] > max_id:
            max_id = message['id']
    return max_id

# Spara till en json fil.
def add(message):
    complete_message = []
    sent = compose()


    '''Add the given message to the list of all messages.
    Then save the updated list of messages to the json file.
    Be sure that the new message also includes an id!'''
    pass