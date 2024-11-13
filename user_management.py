import json

def load_users():
    with open('users.json', 'r') as file:
        return json.load(file)

def authenticate_user(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        return users[username]
    return None

def get_user_role(user):
    return user.get("role", "User")
