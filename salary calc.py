name = input("Enter Name:\n")

salary = input("Enter Monthly Salary:\n")

annual_sal = int(salary) * 12

bonus = (int(salary) * 0.10 * 12 ) + annual_sal

print("Annual Salary = ", annual_sal)
print("Salary After Bonus = ", int(bonus)  )
