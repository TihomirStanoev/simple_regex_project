from regex import RegEx


class Validator:
    """
    Base class for creating validators.

    """

    def __init__(self):
        self.criteria = dict()

    def reset_dict(self):
        for crit in self.criteria:
            self.criteria[crit] = False

    def validator(self, string):
        pass

    def check_result(self, string):
        is_valid = self.validator(string)
        self.reset_dict()
        return is_valid


class PasswordValidator(Validator):
    """
    A class for validating password strength based on specific criteria.
    """

    def __init__(self):
        super().__init__()
        self.criteria = {
            'Be at least 8 characters long': False,
            'Contain one uppercase letter': False,
            'Contain one number': False,
            'Contain one special character (@$!%*?&)': False
        }

    def validator(self, password: str) -> bool:
        self.criteria['Be at least 8 characters long'] = RegEx.is_eight_char.search(password)
        self.criteria['Contain one uppercase letter'] = RegEx.is_uppercase.search(password)
        self.criteria['Contain one number'] = RegEx.is_number.search(password)
        self.criteria['Contain one special character (@$!%*?&)'] = RegEx.is_special.search(password)

        return all(self.criteria.values())

    #    def reset_dict(self):
    #        for crit in self.criteria:
    #            self.criteria[crit] = False

    def check_password(self, password: str) -> bool:
        is_valid = self.validator(password)
        self.reset_dict()
        return is_valid


class EmailValidator(Validator):
    """
    A class for validating email addresses based on a regular expression.
    """

    def __init__(self):
        super().__init__()
        self.criteria = {
            'Valid Email': False
        }

    def validator(self, email):
        self.criteria['Valid Email'] = RegEx.is_valid_email.search(email)
        return all(self.criteria.values())

    # def reset_dict(self):
    #     for crit in self.criteria:
    #         self.criteria[crit] = False

    def check_email(self, email: str) -> bool:
        is_valid = self.validator(email)
        self.reset_dict()
        return is_valid
