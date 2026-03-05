#DevOps project 2026
import string
import random

def generate_admin_pass():
    print("--- DevOps Security Tool: Password Generator ---")
    length = int(input("Enter desired password length: "))
    
    # Define characters: letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    
    print(f"Generated Secure Password: {password}")

if __name__ == "__main__":
    generate_admin_pass()
