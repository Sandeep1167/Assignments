valid_username = "john"
valid_password = "password123"
username = input("Enter your username: ")
password = input("Enter your password: ")
while username != valid_username or password != valid_password:
    print("Invalid username or password.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
print("Login successful!")