class Employee:
    def __init__(self, first_name, last_name, designation):
        self.firstName = first_name
        self.lastName = last_name
        self.designation = designation

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstName, self.lastName)


emp1 = Employee('Faisal', 'Hyder', 'Java Dev')
print(emp1.email)
