import random
import string
import datetime
def log_entry(entry_type, password, strength=None, missing=None, length=None):
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
def check_password(password):
    missing = []
    score = 0
    if not (8 <= len(password) <= 12):
        return None, [], "Password length must be 8-12 characters"
    if not password[0].isalpha():
        return None, [], "Password must begin with a letter"
    if any(c.isupper() for c in password):
        score += 1
    else:
        missing.append("Uppercase")
    if any(c.islower() for c in password):
        score += 1
    else:
        missing.append("Lowercase")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        missing.append("Number")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        missing.append("Special Character")
    if score <= 1:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"
    return strength, missing, "Password is in range"
def generate_password(length):
    if not (8 <= length <= 12):
        return None
    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digit_pool = string.digits
    special_pool = string.punctuation
    first_char = random.choice(upper_pool + lower_pool)
    password = (
        random.choice(upper_pool) +
        random.choice(lower_pool) +
        random.choice(digit_pool) +
        random.choice(special_pool)
    )
    remaining_length = length - 5
    all_characters = upper_pool + lower_pool + digit_pool + special_pool
    for _ in range(remaining_length):
        password += random.choice(all_characters)
    password_list = list(password)
    random.shuffle(password_list)
    return first_char + "".join(password_list)