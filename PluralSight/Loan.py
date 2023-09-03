# get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")) # 50,000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your monthly payment be, in dollars?\n")) # 1,000
months = int(input("How many months do you want to see results for?\n")) # 24

monthy_rate = apr/100/12

for i in range(months):
    # calculate interest to pay
    interest_to_pay = money_owed * monthy_rate
    # add interest
    money_owed = money_owed + interest_to_pay
    
    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
    # make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_to_pay, 'was interest.', end=' ')
    print('Now I owe', money_owed)