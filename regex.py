import re


class RegEx:
    password = re.compile(r'([A-Z]+)|(\d+)|([\@\$\!\%\*\?\&]+)|([a-z]+)')