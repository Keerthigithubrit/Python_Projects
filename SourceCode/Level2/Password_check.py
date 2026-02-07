def check_password(password):
    # Initial assign uppercase,lowercase,digit,special is false
    pwd_uppercase = False
    pwd_lowercase = False
    pwd_digit = False
    pwd_special = False

# Validate the codition

    for char in password:
        if char.isupper():
            pwd_uppercase = True
        elif char.islower():
            pwd_lowercase = True
        elif char.isdigit():
            pwd_digit = True
        elif not char.isalnum():
            pwd_special = True
        else:
            return False
    # Check all condition are matching
    if all ([pwd_uppercase,pwd_lowercase,pwd_digit,pwd_special]):
        print("You Password is Strong.")
    else:
        print("Your Password is Weak")

# Get password from user
get_password = input("Enter your password:")
check_password(get_password)
        