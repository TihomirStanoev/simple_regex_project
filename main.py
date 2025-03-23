import re
from validators import PasswordValidator



def main():

    password_validator = PasswordValidator()

    while True:

        print('1. Password validator')
        choose = input('Your choose: ')
        if choose == '1':
            password = input('Your password:')
            is_valid = password_validator.check_password(password)
            print(is_valid)






if __name__ == "__main__":
    main()