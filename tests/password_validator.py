import unittest
from validators import PasswordValidator


class TestPasswordValidator(unittest.TestCase):

    def setUp(self):
        self.password_validator = PasswordValidator()
        self.valid_password = "A@12mKdA"

    def test_short_length_of_password(self):
        self.assertFalse(self.password_validator.check_result('000000'))
        self.assertFalse(self.password_validator.check_result('A!0000'))
        self.assertFalse(self.password_validator.check_result('aA!000'))
        self.assertFalse(self.password_validator.check_result('aaaaaa'))
        self.assertFalse(self.password_validator.check_result('@@@@@@'))
        self.assertFalse(self.password_validator.check_result('11@aA11'))


    def test_uppercase_exist(self):
        self.assertFalse(self.password_validator.check_result('aaaaaaaaa'))
        self.assertFalse(self.password_validator.check_result('aaaaaa12a'))
        self.assertFalse(self.password_validator.check_result('aa!aa'))
        self.assertFalse(self.password_validator.check_result('aa!aaa12a'))

    def test_digit_exist(self):
        self.assertFalse(self.password_validator.check_result('aaaaaaaaa'))
        self.assertFalse(self.password_validator.check_result('AAaaaaaaa'))
        self.assertFalse(self.password_validator.check_result('!!aaaaaaa'))
        self.assertFalse(self.password_validator.check_result('!!aaaA4'))


    def test_special_exist(self):
        self.assertFalse(self.password_validator.check_result('AAa12aaaa'))
        self.assertFalse(self.password_validator.check_result('AAaaa1aa'))


    def test_valid_password(self):
        self.assertTrue(self.password_validator.check_result(self.valid_password))


if __name__ == "__main__":
    unittest.main()