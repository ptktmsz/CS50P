from validator_collection import validators

try:
    email_address = validators.email(input("What's your e-mail address? "))
    print("Valid")
except ValueError:
    print("Invalid")