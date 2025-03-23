from regex import RegEx


class PasswordValidator:
    def __init__(self):
        self.criteria = {
            'Be at least 8 characters long': False,
            'Contain one uppercase letter': False,
            'Contain one number': False,
            'Contain one special character (@$!%*?&)': False
        }

    def validator(self, password):

        self.criteria['Be at least 8 characters long'] = RegEx.is_eight_char.search(password)
        self.criteria['Contain one uppercase letter'] =  RegEx.is_uppercase.search(password)
        self.criteria['Contain one number'] = RegEx.is_number.search(password)
        self.criteria['Contain one special character (@$!%*?&)'] = RegEx.is_special.search(password)

        return all(self.criteria.values())


    def reset_dict(self):
        for crit in self.criteria:
            self.criteria[crit] = False

    def check_password(self, password):
        is_valid = self.validator(password)
        self.reset_dict()
        return is_valid