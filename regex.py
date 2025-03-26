import re


class RegEx:
    """
       A collection of regular expression patterns for common text processing tasks.
    """
    # Password Validation
    is_eight_char = re.compile(r'.{8,}')  # Be at least 8 characters long
    is_uppercase = re.compile(r'[A-Z]+')  # Contain one uppercase letter
    is_number = re.compile(r'\d+')  # Contain one number
    is_special = re.compile(r'[\@\$\!\%\*\?\&]')  # Contain one special character (@$!%*?&)'

    # Email Validator
    is_valid_email = re.compile(
        r'^([^\.\-][A-Za-z0-9\-\_\.]+[^\.\-])@([^\.\-][a-z0-9\-]+[^\.\-]\.[a-z]{2,8}(\.[a-z]{2,8})?)$')

    # Extractor
    extract_email = re.compile(r'\b(([^\.\-\s][a-z0-9\-\_\.]+[^\.\-])@([^\.\-][a-z0-9\-]+[^\.\-])(\.[a-z]{2,8}(\.[a-z]{2,8})?))\b')
    extract_phone = re.compile(r'(\b(\(\d{,3}\))|(\+|0)\d+(\s|\-)\d+\4\d+\4?(\d+)?[^\ ]\b)')
    
