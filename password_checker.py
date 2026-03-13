import random
import string
import datetime
def log_entry(entry_type, password, strength=None, missing=None, length=None):
    """
    Logs a password check or generation event to results.txt.
    
    Args:
        entry_type (str): Either 'Checked' or 'Generated'.
        password (str): The password that was checked or generated.
        strength (str, optional): The strength rating (Weak/Medium/Strong).
        missing (list, optional): List of missing character types.
        length (int, optional): Length of the password.
    """
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
    """
    Analyses a password and returns its strength rating.
    
    Args:
        password (str): The password to evaluate.

    Returns:
        tuple: (strength, missing, message)
            strength (str or None): 'Weak', 'Medium', 'Strong', or None if invalid.
            missing (list): Character types absent from the password.
            message (str): Validation message.
    """
    missing = []
    score = 0
    if len(password) < 8:
        return None, [], "Password length must be at least 8 characters"
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
    """
    Generates a random password of the specified length.
    Ensures at least one uppercase, lowercase, digit, and special character.
    First character is always a letter.
    
    Args:
        length (int): Desired password length (minimum 8).
        
    Returns:
        str or None: Generated password, or None if length is invalid.
    """
    if length < 8:
        return None
    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digit_pool = string.digits
    special_pool = string.punctuation
    all_characters = upper_pool + lower_pool + digit_pool + special_pool
    required = [
        random.choice(upper_pool),
        random.choice(lower_pool),
        random.choice(digit_pool),
        random.choice(special_pool),
    ]
    remaining = [random.choice(all_characters) for _ in range(length - 4)]
    pool = required + remaining
    random.shuffle(pool)
    first_char = random.choice(upper_pool + lower_pool)
    return first_char + "".join(pool[:-1])