import unittest
from validators import EmailValidator


class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.email_validator = EmailValidator()
        self.valid_email = 'my.name@company.com'

    def test_email_name(self):
        self.assertFalse(self.email_validator.check_result('missing-at-symbol.com'))
        self.assertFalse(self.email_validator.check_result('no space @ email.com'))
        self.assertFalse(self.email_validator.check_result('.leadingdot@example.com'))
        self.assertFalse(self.email_validator.check_result('email.com'))
        self.assertFalse(self.email_validator.check_result('missing-at-symbol.com'))
        self.assertFalse(self.email_validator.check_result('missing-at-symbol.com'))

    def test_email_domain(self):
        self.assertFalse(self.email_validator.check_result('trailingdot@example.com.'))
        self.assertFalse(self.email_validator.check_result('user@invalid_domain'))
        self.assertFalse(self.email_validator.check_result('user@domain..com'))
        self.assertFalse(self.email_validator.check_result('user@-domain.com'))

    def test_valid_email(self):
        self.assertTrue(self.email_validator.check_result(self.valid_email))


if '__main__' == __name__:
    unittest.main()
