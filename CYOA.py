print('''.
            /|                                                               
        //^^^  ~~~~^^^^---___                   ^\\            /|              
     /c~~`'     ____          ^^^^             /||\\        /_ _\\             
     ~^^--; _|||    ~~~---___     ~~~~        / '||\\       | |              
         /_/                 --        ~~~__/ ,  | |\\       \\ \\             
        ~                      -        |\\--;' |  |    ;;      | |            
                               |          \\   |    |    /     /  / 
                              |__ \\  \\     ~--|/~~\\/~~|/     /  /             
Art by                   /---_.     \\  \\         |    /      |  |             
  Win Kang              ;-/   ~\\-----   ;         |           |  |            
                         '--\\_,--------'          |          |   |           
                           / ____    _^^^_..       |        -                
                          |       /^       ..      |       _    |            
              /           | ---- |      .           |      _    |             
          6  /__           `     `.      |           |    -    -              
         0+}/ ;~            ` .--  `      |           -__-    -     q\\        
       =( __ /               / ` -_.     /                   -     /`'>       
        /|  |>          _-__ ---^^     /          _---_____--      /^^\\       
      -------          ///  ///__ -__  / -____--~                 / || \\
''')


def game_over():
    print('''                                 
         (                              
         )\\ )        )      )       (   
        (()/(     ( /(     (       ))\\  
         /(_))_   )(_))    )\\  '  /((_) 
        (_)) __| ((_)_   _((_))  (_))   
          | (_ | / _` | | '  \\() / -_)  
           \\___| \\__,_| |_|_|_|  \\___|  
                                        
            )                           
         ( /(                           
         )\\())     )       (    (       
        ((_)\\     /((     ))\\   )(      
          ((_)   (_))\\   /((_) (()\\     
         / _ \\   _)((_) (_))    ((_)    
        | (_) |  \\ V /  / -_)  | '_|    
         \\___/    \\_/   \\___|  |_|                             
         ''')


def winner():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
    ''')


print("Welcome to the Wild Wood, choose your own adventure! \n")
print('''Venture forth into the perilous depths of the 'Wild Wood' where a fearsome dragon has seized a wagon laden 
with gold destined for the castle. To compound matters, the princess herself was traveling with the wagon and has
fallen into the clutches of the beast. Your quest awaits: to vanquish the dragon, rescue the princess, and reclaim the
riches!\n''')
print('''Will you rise to the challenge, brave the terrors of the woods, confront the dragon, and liberate both princess
and treasure for king and country? ''')
answer1 = input("Choose Y or N: ").lower()
if answer1 == "y":
    print("\nCongratulations! Your adventure begins.\n\nYou arrive at the abduction site and discover two directions in "
          "which the dragon could have gone.")
    answer2 = input('Choose left or right: ').lower()
    if answer2 == 'right':
        print("\nYou come to a river. Choose 'swim' to swim across or 'wait' to wait for a boat.")
        answer3 = input("Type 'swim' or 'wait': ").lower()
        if answer3 == 'wait':
            print('\nA boat arrives and carries you across the river to a cave entrance. Choose \'enter\' to enter the '
                  'cave or choose "left" or "right"')
            answer4 = input('Type "enter", "left", or "right": ').lower()
            if answer4 == "right":
                print('\nYou have found the dragon, the princess, and the gold! Quick, choose a weapon to defeat the '
                      'dragon and become the hero!')
                answer5 = input("Type 'sword', 'bow', or 'gun': ").lower()
                if answer5 == 'bow':
                    print('\nGreat choice! The arrow pierces the heart of the dragon, killing it instantly. You have '
                          'defeated the dragon, rescued the princess, and recovered the gold!')
                    winner()
                elif answer5 == 'gun':
                    print('\nOh no! The gun wings the dragon and makes it very, very angry. He crushes the princess in '
                          'a rage and then tears you into bit sized chunks preparing you for it\'s dinner!')
                    game_over()
                else:
                    print('\nOh no! As you approach with your sword, the dragon reaches down and swallows you whole!')
                    game_over()
            elif answer4 == 'left':
                print('\nOh no! You are eaten by an aligator who was resting at the edge of the river!')
                game_over()
            else:
                print('\nOh no! You enter the den of a large and hungry bear and get torn to pieces!')
                game_over()
        else:
            print('\nOh no! Your armor fills with water and you drown!')
            game_over()
    else:
        print('\nOh no! You\'ve stepped off a cliff!')
        game_over()
else:
    print('\nCoward! You\'ve been stripped of your title, your lands have been seized, and you\'re hereby banished '
          'from the land!')
    game_over()
