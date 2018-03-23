class Employee:
    def __init__(self, first_name, last_name, designation):
        self.firstName = first_name
        self.lastName = last_name
        self.designation = designation

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstName, self.lastName)

    @property
    def full_name(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split(' ')
        self.firstName = first_name
        self.lastName = last_name

    @full_name.deleter
    def full_name(self):
        self.firstName = None
        self.lastName = None


emp1 = Employee('Faisal', 'Hyder', 'Java Dev')
print(emp1.email)
