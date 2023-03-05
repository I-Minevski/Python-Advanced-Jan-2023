class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = ['.com', '.bg', '.net', '.org']

while True:
    email = input()

    if email == "End":
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        index_At = email.index('@')
        name = email[:index_At]
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        else:
            if email.split('.')[-1] not in domains:
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
            else:
                print("Email is valid")