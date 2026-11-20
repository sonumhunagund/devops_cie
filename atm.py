import sys


balance = int(sys.argv[1])
deposit = int(sys.argv[2])
withdrawal = int(sys.argv[3])


finalamount = balance + deposit
updatedamount = finalamount - withdrawal


print("finalamount:", finalamount)
print("updatedamount:", updatedamount)