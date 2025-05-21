x = int(input("Enter your monthly income: "))
y = int(input("Enter your total monthly expenses: "))
monthly_savings = x - y
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest is: $", annual_savings)