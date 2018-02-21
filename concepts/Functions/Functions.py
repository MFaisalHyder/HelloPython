daysWorked = int(input("Enter the days employee worked \n"))
chargePerDay = int(input("Enter the per day cost of labour \n"))
taxDeduction = int(input("Enter the percent of tax to be deducted for PF \n"))


def calculate_pay(daysWorked, chargePerDay, taxDeduction):
    if daysWorked > 0 and chargePerDay > 0 and taxDeduction > 0:
        salary = (daysWorked * chargePerDay)
        salary = salary - (salary * taxDeduction / 100)
        return salary


monthlySalary = calculate_pay(daysWorked, chargePerDay, taxDeduction)
print("Salary for current month is %d" % monthlySalary)
