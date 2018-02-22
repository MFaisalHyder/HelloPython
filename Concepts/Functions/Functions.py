daysWorked = int(input("Enter the days employee worked \n"))
chargePerDay = int(input("Enter the per day cost of labour \n"))
taxDeduction = int(input("Enter the percent of tax to be deducted for PF \n"))


def calculate_pay(days_worked, charge_per_day, tax_deduction):
    if days_worked > 0 and charge_per_day > 0 and tax_deduction > 0:
        salary = (days_worked * charge_per_day)
        salary = salary - (salary * tax_deduction / 100)
        return salary


monthlySalary = calculate_pay(daysWorked, chargePerDay, taxDeduction)
print("Salary for current month is %d" % monthlySalary)
