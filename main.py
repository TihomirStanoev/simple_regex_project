from validators import PasswordValidator, EmailValidator


def validator_result(string, validator_object):
    is_valid = validator_object.check_result(string)
    return is_valid


def main():
    password_validator = PasswordValidator()
    email_validator = EmailValidator()

    print('Validate & Extract Data with Python REGEX!')
    while True:

        print('1. Password validator')
        print('2. Email validator')

        choose = input('Your choose: ')
        if choose == '1':
            password = input('Your password:')
            print(validator_result(password, password_validator))

        elif choose == '2':
            email = input('Your email: ')
            print(validator_result(email, email_validator))


if __name__ == "__main__":
    main()
