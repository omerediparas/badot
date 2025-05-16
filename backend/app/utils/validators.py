import re

def is_valid_email(email):
    """Validate email format."""
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None

def is_strong_password(password):
    """
    Validate password strength.
    Criteria: At least 8 characters, includes a number, uppercase, lowercase, and symbol.
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def are_required_fields_present(data, required_fields):
    """Check if all required fields exist and are non-empty in the data dict."""
    return all(data.get(field) for field in required_fields)

def do_passwords_match(password, confirm_password):
    """Check if password and confirmPassword match."""
    return password == confirm_password
