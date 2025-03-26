import unittest
from validators import PasswordValidator


class TestPasswordValidator(unittest.TestCase):

    def setUp(self):
        self.password_validator = PasswordValidator()
        self.valid_password = "A@12mKdA"

    def test_short_length_of_password(self):
        self.assertFalse(self.password_validator.check_result('000000'))
        self.assertFalse(self.password_validator.check_result('A#0000'))
        self.assertFalse(self.password_validator.check_result('aA#000'))
        self.assertFalse(self.password_validator.check_result('aaaaaa'))
        self.assertFalse(self.password_validator.check_result('@@@@@@'))
        self.assertFalse(self.password_validator.check_result('11@aA11'))
        self.assertTrue(self.password_validator.check_result(self.valid_password))


    def test_uppercase_exist(self):
        pass

    def test_digit_exist(self):
        pass

    def test_special_exist(self):
        pass

    def test_valid_password(self):
        pass







if __name__ == "__main__":
    unittest.main()