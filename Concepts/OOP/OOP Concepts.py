# [class]
class Employee:

    # [function] This is predefined method which is equivalent to Constructor in Java
    def __init__(self, first_name, middle_name, last_name, employee_number, employee_designation, salary):
        self.firstName = first_name
        self.middleName = middle_name
        self.lastName = last_name
        self.employeeNumber = employee_number
        self.designation = employee_designation
        self.salary = salary

    # Every function has instance as first argument by default
    def employee_info(self):
        return '{} {} working as {}'.format(self.firstName, self.lastName, self.designation)


employeeFaisal = Employee('Muhammad', 'Faisal', 'Hyder', 'RC_10000386', 'Software Engineer', 99999999)

print(employeeFaisal.employee_info())
# methods are transformed into class_name.method_name(instance)
# i.e. Employee.employee_info(employeeFaisal)
