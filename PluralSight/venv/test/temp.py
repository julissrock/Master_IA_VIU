acronym = input("What would you like to add?\n")
definition = input("What is the definition?\n")
with open ('test.txt', 'a') as file:
    file.write('\n'+ acronym + ' - ' + definition + '\n')