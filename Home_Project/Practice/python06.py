username = "admin"
password = "Admin1234"

input_username = input("Enter your username: ")
input_password = input("Enter password: ")

while input_password != password:
    print("Invalid password!")
    input_password = input("Enter password again: ")

print("Login successfully!")
