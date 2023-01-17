import random
import string

# Ask the user for the desired length of the password
while True:
    length = int(input("How many characters long would you like your password to be (minimum 8)? "))
    if length >= 8:
        break
    else:
        print("Password should be at least 8 characters long.")

# Ask the user for the number of letters and numbers in the password
letters = int(input("How many letters would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

# Generate a password with a mix of upper and lowercase letters, numbers, and symbols
password = ""
password += "".join(random.choice(string.ascii_letters) for i in range(letters))
password += "".join(random.choice(string.digits) for i in range(numbers))
password += "".join(random.choice(string.punctuation) for i in range(length - letters - numbers))

# Shuffle the password
password = ''.join(random.sample(password, len(password)))

# Print the password
print("Your new password is: ", password)
