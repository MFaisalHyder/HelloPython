class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, middle_name, last_name, employee_number, employee_designation, salary):
        self.firstName = first_name
        self.middleName = middle_name
        self.lastName = last_name
        self.employeeNumber = employee_number
        self.designation = employee_designation
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


# This is the syntax to inherit a class in Python.
class Developer(Employee):
    raise_amount = 1.15


faisalDev = Employee('Muhammad', 'Faisal', 'Hyder', 'RC_10000386', 'Software Engineer', 81000)
# faisalDev = Developer('Muhammad', 'Faisal', 'Hyder', 'RC_10000386', 'Software Engineer', 81000)

# This functions helps to visualize easily the hierarchy of inherited class and Method resolution order
# print(help(Developer))

print(faisalDev.salary)
faisalDev.apply_raise()
print(faisalDev.salary)
