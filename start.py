import time
from utilities import misc
import battle

print('''

 =============================
| FINAL FANTASY TACTICS - CLI |
 =============================

 created by Michael Law [github.com/FlyingGeese]

 ** Quit game at any time by pressing CTRL + C **

''')

time.sleep(2.3)


def begin_game():
    main = input('''
    
    I am Arazlam, student of Ivalice's Middle Age. You are familiar with the War of
    the Lions, no?

    It was a bitter war of succession that rent the land of Ivalice in two. Here we
    first find mention of Delita Heiral, a hithertofore unknown young man, the hero
    who would draw the curtain of this dark act of our history.
    
    His is a heroism of great renown - a story familiar to all who dwell within our 
    land.
    
    Ah, but what the eye sees is oftentimes a mere fragment of the truth.
    
    There was another young man, the youngest of House Beoulve, long famed for 
    producing leaders of knights and men.
    
    There is no official record of the role he played on history's stage.
    
    However, according to the Durai Papers, the existence of which became known to
    the public only this last year - they had long lain concealed in Church 
    archives - this forgotten young man is in fact the true hero.
    
    The Church maintains he was a heretic, an inciter of unrest and disturber of 
    the peace.
    
    Which accounts is to be believed?
    
    Join me in my search to uncover the answer.
    
    Ah, but before we begin, might I ask you to share with me your name and the 
    date of your birth?
    
    ''')
    while not bool(main) or main.strip() == '':
        main = input('Sorry, I didn\'t get that ... What was the name again?:\n')

    main_dob = input(f'\nOn what day was {main} born?\n')

    print(f'''
    
    Prepare for battle, {main}!
    
    ''')

    battle.start_battle()

# @misc.typewrite
begin_game()