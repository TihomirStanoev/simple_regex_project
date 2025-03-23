import re


class RegEx:
    # Password Validation
    is_eight_char = re.compile(r'.{8,}') # Be at least 8 characters long
    is_uppercase = re.compile(r'[A-Z]+') # Contain one uppercase letter
    is_number = re.compile(r'\d+') # Contain one number
    is_special = re.compile(r'[\@\$\!\%\*\?\&]') # Contain one special character (@$!%*?&)'