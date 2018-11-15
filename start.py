print('''

 =============================
| FINAL FANTASY TACTICS - CLI |
 =============================

 created by Michael Law [github.com/FlyingGeese]

 ** Quit game at any time by pressing CTRL + C **

''')

main = input('Choose a name for your main character:\n')
while not bool(main) or main.strip() == '':
    main = input('Sorry, I didn\'t get that ... What was the name again?:\n')

main_dob = input(f'\nOn what day was {main} born?\n')

print(f'''

Prepare for battle, {main}!

''')