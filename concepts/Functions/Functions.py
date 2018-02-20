daysWorked = int(input(print("Enter the days employee worked")))
chargePerDay = int(input(print("Enter the per day cost of labour")))
taxDeduction = int(input(print("Enter the percent of tax to be deducted for PF")))


def calculate_pay(daysWorked, chargePerDay, taxDeduction):
    if daysWorked > 0 and chargePerDay > 0 and taxDeduction > 0:
        salary = (daysWorked * chargePerDay)
        salary = salary - (salary * 100 / taxDeduction)
        return salary


monthlySalary = calculate_pay(daysWorked, chargePerDay, taxDeduction)
print("Salary for current month is %d" % monthlySalary)
