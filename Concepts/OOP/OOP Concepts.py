# [class]
class Employee:
    # class variable, instances can also access it, if the same is not defined for their own scope
    raise_amount = 1.05

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

    def increment(self):
        self.salary = int(Employee.raise_amount * self.salary)


employeeFaisal = Employee('Muhammad', 'Faisal', 'Hyder', 'RC_10000386', 'Software Engineer', 81000)
employeeShane = Employee('Shane', 'Mathew', 'Corey', 'AV_10000886', 'Software Engineer', 85000)

print(employeeFaisal.employee_info())
# methods are transformed into class_name.method_name(instance)
# i.e. Employee.employee_info(employeeFaisal)

employeeShane.raise_amount = 1.04
print("Faisal's salary", employeeFaisal.salary)
print("Increment for Faisal : ", employeeFaisal.raise_amount, employeeFaisal.increment())
print("Faisal's salary after increment", employeeFaisal.salary)

print("Shane's salary", employeeShane.salary)
print("Increment for Shane : ", employeeShane.raise_amount, employeeShane.increment())
print("Shane's salary after increment", employeeShane.salary)

# To check if an instance contains variable or what are the attributes of an instance run following
# employeeFaisal.__dict__