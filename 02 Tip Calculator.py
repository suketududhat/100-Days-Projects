print("Welcome to the tip calculator:")

total_bill = input("What was the total bill? $")
tip = input("What % tip would you like to give?")
no_of_people = input("How many people are splitting the bill+tip?")

bill_with_tip = float(total_bill)*(1+(int(tip)/100))
split_bill = round(bill_with_tip/int(no_of_people), 2)

print(f"Each person should pay: {split_bill}")