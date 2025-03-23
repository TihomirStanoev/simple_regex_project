from regex import RegEx


class PasswordValidator:
    def __init__(self, password):
        self.password = password
        self.pass_len = 8
        self.strong_password = {
            'Be at least 8 characters long': False,
            'Contain one uppercase letter': False,
            'Contain one number': False,
            'Contain one special character (@$!%*?&)': False
        }

    def validator(self):

        is_valid = False
        criteria = RegEx.password.findall(self.password)

        if len(self.password) >= self.pass_len:
            self.strong_password['Be at least 8 characters long'] = True

        for uppercase, number, special, char in criteria:
            if uppercase:
                self.strong_password['Contain one uppercase letter'] = True
                continue
            if number:
                self.strong_password['Contain one number'] = True
                continue
            if special:
                self.strong_password['Contain one special character (@$!%*?&)'] = True
                continue





    def reset_criteria(self):

        for criteria, value in self.strong_password.items():
            self.strong_password[criteria] = False
