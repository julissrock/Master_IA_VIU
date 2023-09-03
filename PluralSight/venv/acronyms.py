def find_acronym():
    loook_up = input("What would you like to look up?\n")
    found = False
    try:
        with open ('acronyms.txt') as file:
            for line in file:
                if loook_up in line:
                    print(line)
                    found = True
                    break
        if not found:
                print("Sorry, I don't know that one.")
    
    except FileNotFoundError as e:
        print('File not found')
        return
            
def add_acronym():
    acronym = input("What would you like to add?\n")
    definition = input("What is the definition?\n")
    with open ('acronyms.txt', 'a') as file:
        file.write('\n'+ acronym + ' - ' + definition + '\n')

def main():
    #Ask the user if they want to look up an acronym or add an acronym
    choice = input("Would you like to look up an acronym (L) or add an acronym (A)?\n")
    if choice == 'L' or choice == 'l':
        find_acronym()
    elif choice == 'A' or choice == 'a':
        add_acronym()

main()
        