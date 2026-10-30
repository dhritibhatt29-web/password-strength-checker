
import re

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase letters
if re.search("[A-Z]", password):
    score += 1

# Check lowercase letters
if re.search("[a-z]", password):
    score += 1

# Check numbers
if re.search("[0-9]", password):
    score += 1

# Check special characters
if re.search("[!@#$%^&*]", password):
    score += 1

# Display password strength
print("\nPassword Score:", score, "/ 5")

if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MODERATE")

else:
    print("Password Strength: STRONG")

