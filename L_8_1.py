import re
#address = 'someone@geekbrains.ru'
def email_parse(email_address):
    if  not re.findall(r'^\w+[@]\w+\.\w+$', email_address):
        print(f'ValueError: wrong email: {email_address}')
    else:
        print({'username': re.split('@', email_address)[0], 'domain': re.split('@', email_address)[1]})
    return
email_parse('someone@geekbrains.ru')
