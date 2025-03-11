firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

if firstName and lastName:
    print(f"Welcome, {firstName} {lastName}!")

else:
    print("Error: Both first name and last name must be provided: ")
