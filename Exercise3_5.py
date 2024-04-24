income = 58200

if income <= 67000:
    tax = 0.24 * income
   # income - tax
    actual_income = income - tax
    
    print(actual_income)

elif income <= 97000:
    tax = 0.31 * income
    actual_income = income - tax
    print(actual_income)

else:
    tax = 0.34 * income
    actual_income = income - tax
    print(actual_income)
