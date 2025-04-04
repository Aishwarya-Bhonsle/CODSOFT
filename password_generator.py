import random
import string

# Function to generate a random password
def generate_password(length=12, strength="medium"):
    # Character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Determine character sets based on strength
    if strength == "weak":
        all_characters = lowercase_letters + digits  # Lowercase letters and digits only
    elif strength == "strong":
        all_characters = lowercase_letters + uppercase_letters + digits + punctuation  # All character sets
    else:  # medium strength (default)
        all_characters = lowercase_letters + uppercase_letters + digits  # Lowercase, uppercase, and digits

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Function to evaluate the strength of the password
def evaluate_password_strength(password):
    # Weak password criteria
    
    # Check for the presence of lowercase, uppercase, digits, and punctuation
    has_lowercase = any(c in string.ascii_lowercase for c in password)
    has_uppercase = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_punctuation = any(c in string.punctuation for c in password)
# Ask the user for desired password strength
print("Select desired password strength:")
print("1. Weak ")
print("2. Medium ")
print("3. Strong ")

strength_choice = input("Enter your choice (1/2/3): ")

# Map user choice to strength level
if strength_choice == "1":
    strength = "weak"
elif strength_choice == "2":
    strength = "medium"
elif strength_choice == "3":
    strength = "strong"
else:
    print("Invalid choice! Defaulting to medium strength.")
    strength = "medium"

# User input for password length
length = int(input("Enter the desired password length: "))

# Generate password
password = generate_password(length, strength)

# Evaluate password strength
strength = evaluate_password_strength(password)

# Display the results
print(f"Generated password: {password}")
