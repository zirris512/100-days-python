print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

split_total = (total * (1 + tip / 100)) / people

print(f"Each person should pay: ${split_total:.2f}")
