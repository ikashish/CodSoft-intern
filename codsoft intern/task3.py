#PASSWORD GENERATOR
import random
import string

length = int(input("Enter the desired length of the password : "))
uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes' 
symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'


characters = string.ascii_lowercase  

if uppercase:
    characters += string.ascii_uppercase
if numbers:
    characters += string.digits
if symbols:
    characters += string.punctuation


password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password is : ", password)