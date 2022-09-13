annualIncome = int(input("Enter Annual Income\n"))
if annualIncome<=250000:
    print("NO TAX")
elif annualIncome>250000 and annualIncome<=500000:
    tax=annualIncome*5/100
    print("Income tx Amnt="+str(tax))
elif annualIncome>500000 and annualIncome<=1000000:
    tax=annualIncome*20/100
    print("Income tx Amnt="+str(tax))
else:
    tax=annualIncome*30/100
    print("Income tx Amnt="+str(tax))