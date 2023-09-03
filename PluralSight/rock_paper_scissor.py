import random
computer_choice = random.choice(['rock', 'paper', 'scissor'])
user_choice = input('Do you want - rock, paper or scissor?\n')
print('Computer chose ' + computer_choice)
if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('Computer wins!')
elif user_choice == 'rock' and computer_choice == 'scissor':
    print('User wins!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('User wins!')
elif user_choice == 'paper' and computer_choice == 'scissor':
    print('Computer wins!')
elif user_choice == 'scissor' and computer_choice == 'rock':
    print('Computer wins!')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('User wins!')
else:
    print('This is not a valid object selection!')  
    