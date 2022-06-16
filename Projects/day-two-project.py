# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people split the bill?"))

total = (tip / 100 * bill + bill) / people
total_bill = round(total, 2)
# format = "{:.2f}".format(total_bill)
print(f"\nEach person should pay: ${total_bill}")