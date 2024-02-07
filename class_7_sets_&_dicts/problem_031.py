user_creds = {}
for i in range(3):
    username = input('Enter your username for login: ')
    password = input('Enter your password for login: ')
    user_creds[username] = password

print(user_creds)