expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0
for x in expenses:
    sum = sum + x
    
print ("You spent $", sum, " on lunch this week.", sep='')  

#Another way to do this
#total = sum(expenses)
#print ("You spent $", total, " on lunch this week.", sep='')  