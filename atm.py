balance = int(input("enter balance:"))
deposit = int(input("enter deposit:"))
withdrawal = int(input("enter withdrawal:"))


finalamount = balance + deposit
updatedamount = finalamount - withdrawal


print("finalamount:", finalamount)
print("updatedamount:", updatedamount)