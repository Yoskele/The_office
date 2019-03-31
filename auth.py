import json


# DONE 
USERS_FILE_PATH = 'data/users.json'
#fixa json 
# fixa en for loop kolla om user finns i listan.
with open('data/users.json', 'r') as f:
    users = json.load(f)

def login(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    else:
        return False
        

    '''Load all users from the json file.
    If a user is found with a matching username AND password,
    return True. Otherwise, return False.'''
