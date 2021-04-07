import re

def email_parse(email_fddress):
    RE_EMAIL = re.compile(r'\w+@\w+\.\w+')


 #   'someone@geekbrains.ru'