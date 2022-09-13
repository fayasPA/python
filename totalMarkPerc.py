totalPercentage = float(input("Enter Total Mark Percentage\n"))
if totalPercentage>=90:
    print("Grade-A")
elif totalPercentage>=80 and totalPercentage<90:
    print("Grade-B")
elif totalPercentage>=70 and totalPercentage<80:
    print("Grade-C")
elif totalPercentage>=60 and totalPercentage<70:
    print("Grade-D")
elif totalPercentage>=50 and totalPercentage<60:
    print("Grade-E")
else:
    print("Grade-Failed")