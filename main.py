strength = "bad"
import sys
def numberCheck(password):
    global numberList
    for char in password:
        if char.isdigit():
            numberList.append(int(char))
def capitalCheck(Password):
    global capitalList
    for Char in Password:
        if Char.isupper():
            capitalList.append(str(Char))
def specialCheck(specialPassword):
    global specialList
    for special in specialPassword:
        if not special.isalnum():
            specialList.append(special)
print("Passwords should be 12 characters long with 2 numbers, capital letters, and special characters.")
while strength == "bad":
    numberList = []
    capitalList = []
    specialList = []
    userPassword = input("Please enter a password: ")
    numberCheck(userPassword)
    specialCheck(userPassword)
    capitalCheck(userPassword)
    if ' ' in userPassword:
        print("Spaces are not allowed in the password.")
        continue
    if "Password" or "password" in userPassword:
        print("Password may not be used in your password.")
        continue
    if len(userPassword)<12:
        print("Your password must be at least 12 characters long.")
        continue
        print("Your password strength is okay.")
    if len(numberList)<2:
        print("Your password must have at least 2 numbers.")
        continue
        print("Your password strength is okay.")
    if len(userPassword)<12:
        print("Your password must be at least 12 characters long.")
        continue
        print("Your password strength is good.")
    if len(specialList)<2:
        print("Your password must have at least 2 special characters")
        continue
        print("Your password strength is good.")
    if len(capitalList)<2:
        print("Your password must have at least 2 capital letters.")
        continue
    strength = "good"
print("Your password strength is excellent.")
sys.exit()
