from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


MIN_LENGTH = 4

valid_domains = ['.com', '.bg', '.org', '.net']

pattern_domain = r'\.[a-z]+'

email = input()

while email != 'End':

    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError('Email must contain only one @!')
        if len(email.split('@')[0]) <= MIN_LENGTH:
            raise NameTooShortError(f'Name must be more than {MIN_LENGTH} characters')
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')
        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

        print('Email is valid')

    except IndexError:
        print('Invalid email')

    email = input()