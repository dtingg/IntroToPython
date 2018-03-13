# Tipper program
# enter a restaurant bill total
# display 15% tip and 20% tip

bill = float(input("How much is your restaurant bill? "))
tip15 = round(bill * .15, 2)
tip20 = round(bill * .20, 2)
print("A 15% tip is ", tip15)
print("and a 20% tip is ", tip20)