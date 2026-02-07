def validate_email(email):
    # Email contains only one @ symbol
    if email.count("@") != 1:
        return False
    
    # Username and domain name split
    username,domain = email.split("@")

    # Username must not empty
    if not username or not domain:
        return False
    
    # Check ". " is available before domain name
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True

# Get input as email
email_address = input("Enter the email address:")
if validate_email(email_address):
    print("Valid Email")
else:
    print("Invalid email")
