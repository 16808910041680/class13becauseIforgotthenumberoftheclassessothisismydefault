def total_calc (bill, amount, tip):
    total = bill + (bill * (tip / 100))
    return round(total / amount, 2)
def main():
    print("Welcome to the tip calculator!")
    bill = float(input("Enter the total bill amount: "))
    amount = int(input("Enter the number of people: "))
    tip = int(input("Enter the tip percentage: "))
    total = total_calc(bill, amount, tip)
    print(f"Each person should pay (including tip): ${total}")
    print ("The total bill is: $", bill)
    print ("The tip is: $", bill * (tip / 100))
    print ("The total amount is: $", bill + (bill * (tip / 100)))
    print ("Each person will be tipping: $", bill * (tip / 100) / amount)
    print ("Each person will be paying (excluding tip): $", bill / amount)

main()

