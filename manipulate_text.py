from regex import RegEx


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



