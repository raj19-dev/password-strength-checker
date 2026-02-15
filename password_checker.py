import random
import string
import datetime
def log_entry(entry_type, password, strength = None, missing = None, length = None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("results.txt", "a") as file:
        file.write("Type: " + entry_type + "\n")
        file.write("Password: " + password + "\n")
        if length is not None:
            file.write("Length: " + str(length) + "\n")
        if strength:
            file.write("Strength: " + strength + "\n")
        if missing is not None:
            if missing:
                file.write("Missing: " + ", ".join(missing) + "\n")
            else:
                file.write("Missing: None\n")
        file.write("Date: " + now + "\n")
        file.write("------------------------------------------\n")
def check_password():
    password = input("Enter your password: ")
    missing = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_spec = False
    has_space = False
    score = 0
    for ch in password:
        if ch.isupper():
          has_upper = True
        if ch.islower():
          has_lower = True
        if ch.isdigit():
          has_digit = True
        if ch in string.punctuation:
          has_spec = True
        if ch == ' ':
          has_space = True
    if 8 <= len(password) <= 12:
        print("Password is in range")
    else:
        print("Password length invalid")
        exit()
    if has_upper:
        score += 1
    else:
        print("Missing uppercase")
        missing.append("Uppercase")
    if has_lower:
        score += 1
    else:
        print("Missing lowercase")
        missing.append("Lowercase")
    if has_digit:
        score += 1
    else:
        print("Missing number")
        missing.append("Number")
    if has_spec:
        score += 1
    else:
        print("Missing special character")
        missing.append("Special Character")
    if has_space:
        print("Password should not contain spaces")
    if score <= 1:
        print("Password is weak")
        strength = "Weak"
    elif 2 <= score <= 3:
        print("Password is medium")
        strength = "Medium"
    else:
        print("Password is strong")
        strength = "Strong"
    log_entry("Checked", password, strength, missing, len(password))
def generate_password():
    length = int(input("Enter password length:"))
    if (length < 8):
        print ("Password is too short!")
    elif (length > 12):
        print ("Password is too long!")
    else:
        upper_pool = string.ascii_uppercase
        lower_pool = string.ascii_lowercase
        digit_pool = string.digits
        special_pool = string.punctuation
        upper_char = random.choice(upper_pool)
        lower_char = random.choice(lower_pool)
        digit_char = random.choice(digit_pool)
        special_char = random.choice(special_pool)
        remaining_length = length - 4
        all_characters = upper_pool + lower_pool + digit_pool + special_pool
        remaining_chars = ""
        for i in range(remaining_length):
            remaining_chars += random.choice(all_characters)
        password = upper_char + lower_char + digit_char + special_char + remaining_chars
        password_list = list(password)
        random.shuffle(password_list)
        final_password = "".join(password_list)
        print ("Generated Password:", final_password)
        log_entry("Generated", final_password, "Strong", None, length)
print ("Enter 1 for Password Strength Checker")
print ("Enter 2 to generate a random password")
choice = input("Enter your choice:")
if (choice == '1'):
    check_password()
elif (choice == "2"):
    generate_password()
else:
    print("Invalid input")

