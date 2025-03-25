from manipulate_text import Extractor
from validators import PasswordValidator, EmailValidator


def validator_result(string, validator_object):
    is_valid = validator_object.check_result(string)
    return is_valid


def main():
    password_validator = PasswordValidator()
    email_validator = EmailValidator()
    extractor = Extractor()
    result = ''

    print('Validate & Extract Data with Python REGEX!')
    while True:

        print('1. Password validator')
        print('2. Email validator')
        print('3. Find email')
        print('4. Find phone')
        print('5. Extract emails and phones')

        choose = input('Your choose: ')
        if choose == '1':
            password = input('Your password:')
            result = validator_result(password, password_validator)

        elif choose == '2':
            email = input('Your email: ')
            result = validator_result(email, email_validator)

        elif choose == '3':
            extractor.text = input('Enter text: ')
            result = extractor.extract_email()

        elif choose == '4':
            extractor.text = input('Enter text: ')
            result = extractor.extract_phone()

        elif choose == '5':
            extractor.text = input('Enter text: ')
            result = extractor.extract_phone_and_email()

        else:
            break

        print(result)


if __name__ == "__main__":
    main()
