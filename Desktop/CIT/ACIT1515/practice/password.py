username = input('What is your username: ')
password = input('Enter your password: ')
length_password = len(password)
secret = '*' * length_password
# secret = password(input, len(input) * '*')
print(f'{username}, your password {secret} is {length_password} letters long')