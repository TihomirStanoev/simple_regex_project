from regex import RegEx
import re


class Extractor:
    """
    A class for extracting email addresses and phone numbers from a given text.
    """

    def __init__(self, text=''):
        self.text = text

    def extract_phone_and_email(self):
        extracted_emails = self.extract_email()
        extracted_phones = self.extract_phone()
        return extracted_emails, extracted_phones

    def extract_email(self) -> list:
        emails = RegEx.extract_email.findall(self.text)
        return [email[0] for email in emails]

    def extract_phone(self) -> list:
        phones = RegEx.extract_phone.findall(self.text)
        return [phone[0] for phone in phones]


class StringProcessor(Extractor):
    """
    A class for processing and manipulating strings, extending the Extractor class.

    This class provides methods for text manipulation, such as replacing words
    using regular expressions with optional flags for case-insensitivity or verbose mode.
    """

    def __init__(self):
        super().__init__()

    def replace_word(self, old_word, new_word, rex_flag):
        rex_flag = re.I if rex_flag == '1' else re.X
        return re.sub(rf'{old_word}', new_word, self.text, flags=rex_flag)
