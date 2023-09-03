# for i in range(0,7,2):
#     print(i)
# for j in range(10,80,10):
#     print(j)

Total=0
expenses = []
num_expenses = int(input("Enter # of expenses: "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))
    Total = Total + expenses[i]
print("You spent $", Total, " on lunch this week.", sep='') 