from unicodedata import name


class Meta:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.list_of_people = []

    def get_name(self):
        return self.name
    @property
    def get_email(self):
        return self.email


obj = Meta("Someone", 'some@gmail.com')
data = obj.get_name()
print(data)

email = obj.get_email
print(email)