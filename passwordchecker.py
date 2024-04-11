# Minimum password length
min_length = 8

# Get password from the user
password = input("Enter your password: ")

# Check password length
if len(password) < min_length:
  print("Password is too short. Minimum length is", min_length, "characters.")
  exit()

# Check for uppercase, lowercase, and numbers
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

# Check if all requirements are met
if not (has_uppercase and has_lowercase and has_number):
  print("Password must contain uppercase letters, lowercase letters, and numbers.")
else:
  print("Password is valid.")
