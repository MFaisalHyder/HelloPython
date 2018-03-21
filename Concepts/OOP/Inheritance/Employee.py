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

    def employee_info(self):
        return self.firstName + ' ' + self.lastName

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}', {})".format(self.firstName, self.middleName, self.lastName,
                                                                   self.employeeNumber, self.designation, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.firstName, self.designation);

    # operator overloading for objects of type Employee
    def __add__(self, other):
        return self.salary + other.salary


# This is the syntax to inherit a class in Python.
class Developer(Employee):
    raise_amount = 1.15

    # Constructor of Developer class
    def __init__(self, first_name, middle_name, last_name, employee_number, employee_designation, salary,
                 programming_lang):
        pass
        # There are two ways to let Parent's constructor handle initialization of common field, & achieve DRY principle
        # 1st
        super().__init__(first_name, middle_name, last_name, employee_number, employee_designation, salary)
        # 2nd
        # Employee.__init__(self, first_name, middle_name, last_name, employee_number, employee_designation, salary)
        self.programming_lang = programming_lang


class Manager(Employee):
    def __init__(self, first_name, middle_name, last_name, employee_number, employee_designation, salary,
                 employees_list=None):
        # it is better to set mutable data types with None in parameters list
        super().__init__(first_name, middle_name, last_name, employee_number, employee_designation, salary)
        if employees_list is None:
            self.employees_list = []
        else:
            self.employees_list = employees_list

    def hire_employee(self, employee):
        if employee not in self.employees_list:
            self.employees_list.append(employee)

    def terminate_employee(self, employee):
        if employee in self.employees_list:
            self.employees_list.remove(employee)

    def reporting_employees(self):
        for employee in self.employees_list:
            print(employee.employee_info())


faisalDev = Employee('Muhammad', 'Faisal', 'Hyder', 'RC_10000386', 'Software Engineer', 165000)
faisalPythonDev = Developer('Muhammad', 'Faisal', 'Hyder', 'PyLab_11', 'Software Engineer', 165000, 'Python')
faisalJavaDev = Developer('Muhammad', 'Faisal', 'Hyder', 'Av_11', 'Software Engineer', 185000, 'Java')

manager = Manager('Muhammad', 'Ghazanfer', 'Ali', '360_Factors', 'Architect', 550000, [faisalPythonDev, faisalJavaDev])

# This functions helps to visualize easily the hierarchy of inherited class and Method resolution order
# print(help(Developer))

print(faisalDev.salary)
faisalDev.apply_raise()
print(faisalDev.salary)

print(faisalJavaDev.programming_lang)
# print(faisalDev.programming_lang) parent cannot access child's scope attributes
print(faisalPythonDev.programming_lang)

manager.reporting_employees()

# method to find out if given object is an instance of a given Class or not
print('Is faisalJavaDev a Developer', isinstance(faisalJavaDev, Developer))
print('Is faisalJavaDev an Employee', isinstance(faisalJavaDev, Employee))

print('Is manager a Developer', isinstance(manager, Developer))
print('Is manager a Employee', isinstance(manager, Employee))

# this is also a method to find if the class is sub class of given class.
print('Developer class is subclass of Employee class', issubclass(Developer, Employee))

# Special Methods [also called Magic or Dunder methods; because they are usually surrounded by __func_name__]
# These methods allow to change some builtin behaviour
# Most common example is __init__ method.
# https://docs.python.org/3/reference/datamodel.html#special-method-names
"""
Two other common methods are 
__repr__: un ambiguous representation of an Object
__str__: readable presentation of an Object

__repr__ is required, if we use 'str' but have only 'repr' defined then 'str' falls back to implementation of 'repr'
"""

print(faisalDev)  # if 'str' is provided then it will be used as default representation of object else 'repr' is used

# print(repr(faisalDev))  # before repr it just prints information about memory location of given object
# print(str(faisalDev))

# this 'add' dunder method is supported by int and str both to perform operator overloading
print(int.__add__(1, 5))
print(str.__add__('Xiaomi', ' - Redmi 5 Plus'))

print('Combined salary for Java & Python role = ', faisalJavaDev + faisalPythonDev)
