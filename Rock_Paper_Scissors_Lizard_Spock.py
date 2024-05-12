import random

# Rock, Paper, Scissors, Lizard, Spock - shartlesville
restart = True
while restart:

    def game():
        rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

        #  Write your code below this line 👇

        lizard = '''
                                      @@@@@@@                       
                                @@@@@@@@@@@@@@@                   
                           @@@@@@@          @@@@@@              
                        @@@@@      @@@@@@@@     @@@@@@          
                     @@@@@@  @@@@@@@@@@@@@@@@@@    @@@@@@       
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@       
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
                    @@@@@@@@@@                   @@@@@@         
                    @@@@@@@@                                    
                    @@@@@@@@@@             @@@@@@               
                   @@@@@@@@@@@@@     @@@@@@@@@@@              
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@                                  
                  @@@@@@@@@@@@@@@@@@@@@@@@@                                         
                  @@@@@@@@@@@@@@@@@@@@@                             
                  @@@@@@@@@@@@@@@@@@                                
                   @@@@@@@@@@@@@@@@                              
        '''

        # noinspection SpellCheckingInspection
        spock = '''
                                     ojou                                 
                                    j8WWW3d                                
                            uoou   j3LLLLQ3d                               
                          j83QW38jjd3LLLLLQdo                              
                         j8QLLLLQ3888LLLLLQ8d         j888j                
                         d3QLLFLL3888QLLLLL38        odWQLQ3d               
                         d3QLLFLLQ888WLLLLLQdu       d3QLLLW8u              
                         j3QLLLFLL3883LFLLLQ8j      udWLLLLW8u              
                         j8QLFLFFLQ888LLFLLL38      d8QLFFL38 d838d               
                         odWLLLFLLQ388QLFLLLW8u     83LLFLL38d8338d               
                          odWLLFFLLQW88QLFLLLW8    83LLLLLW88WLLLL8        
                          uj3LLFFLFLQ88QLLLFFQ3    8WLLFLL388QLLLQ8        
                           j3QLLFFFFL88WLLFLFL3   j8LLFFLQ88WLLLLW        
                           j3LLFFFFLQ88QLFLLLQ388WLFFLLW83LLLLQ8j               
                  ujdddo     83LLFFFFLQ3WLLFLLLW83LFLLLQ88LLLLLWd          
                 d8WQQWW8o   j8LLLLLFLLLLLFFLFLLQLLFLLLW8WLLLLQ3d          
                 8QLLLLLQ3du o8QLLFFFLFFFFLFLFFFFFFLFFLLQLLLLLQd          
                 83QLLFLLL3djj8QLLFFFFFLFFFFLFFFFFFLFFFLLLFFLLWd         
                 udWLLLFLFL3888LLFFFFFFFLLLFFLFLFFFFFLFFFLFLLLWj8           
                  jdWLLFLLLLW88LLLLLLLLFLFFFFFFFLFFLFFFLLFFFFLWd6          
                   jd3QLLFLLFLLQW3388WQLLLFFFLFFLFLFFFFLFLFLFLWd3         
                     ud3LLLLLLFFFFFLLLQ38WLLFLLFFFFFFFFFLFFLFLQd          
                      83LLLLLFFFFFFLLLLWWLLFFFFLFLFFLFFFLFLFFdj                    
                         odWLLFFLFL83333333338FFFLFLFLFLFFFLL8           
                          j8WLFFFFL83333333338FLFFFFFLFFFLFd
                            ud8QLLLLF83333333338FFFFLLLL3du              
                              od3QLFLFFFFFFFFLFFLFFFLFLQ88                
                                uj8WLLFLFFFFFFLFLFLLFLW8j                 
                                  d3LLLFFLFLFFFFFFLFLW8j           
                                  u8WLLLLLLLFLLLLLLLLLW8o                  
                                  u88333333333333833838do                                   
        '''

        print("\nPlease enter the number corresponding to your choice: 0 for Scissors, 1 for Paper, 2 for Rock, "
              "3 for Lizard, or 4 for Spock. Choose wisely!")

        computer_choice = random.randint(0, 4)

        try:
            user_input = int(input("Your choice is: "))
            if user_input == 0:
                print(f'\nYou chose scissors\n{scissors}')
            elif user_input == 1:
                print(f'\nYou chose paper\n{paper}')
            elif user_input == 2:
                print(f'\nYou chose rock\n{rock}')
            elif user_input == 3:
                print(f'\nYou chose lizard\n{lizard}')
            elif user_input == 4:
                print(f'\nYou chose Spock\n{spock}')
            elif user_input < 0 or user_input > 4:
                print("Invalid choice. Please enter a value between 0 and 4.")
                user_input = int(input("Your choice is: "))
                try:
                    if user_input == 0:
                        print(f'\nYou chose scissors\n{scissors}')
                    elif user_input == 1:
                        print(f'\nYou chose paper\n{paper}')
                    elif user_input == 2:
                        print(f'\nYou chose rock\n{rock}')
                    elif user_input == 3:
                        print(f'\nYou chose lizard\n{lizard}')
                    elif user_input == 4:
                        print(f'\nYou chose Spock\n{spock}')
                    elif user_input < 0 or user_input > 4:
                        print("Invalid choice. Game over!")
                except ValueError:
                    print("Invalid input. Game over.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_input = int(input("Your choice is: "))

        if computer_choice == 0:
            print(f'Computer chose scissors\n{scissors}')
        elif computer_choice == 1:
            print(f'Computer chose paper\n{paper}')
        elif computer_choice == 2:
            print(f'Computer chose rock\n{rock}')
        elif computer_choice == 3:
            print(f'Computer chose lizard\n{lizard}')
        else:
            print(f'Computer chose Spock\n{spock}')

        if computer_choice == user_input:
            print(f'It\'s a tie! You both chose {computer_choice}.\n')
        elif (computer_choice == 0 and user_input == 1) or (user_input == 0 and computer_choice == 1):
            print(f'Scissors cut Paper\n')  # Scissors cuts Paper
            if computer_choice == 0:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 1 and user_input == 2) or (user_input == 1 and computer_choice == 2):
            print(f'Paper covers rock.\n')  # Paper covers Rock
            if computer_choice == 1:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 2 and user_input == 3) or (user_input == 2 and computer_choice == 3):
            print(f'Rock crushes lizard.\n')  # Rock crushes Lizard
            if computer_choice == 2:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 3 and user_input == 4) or (user_input == 3 and computer_choice == 4):
            print(f'Lizard poisons Spock.\n')  # Lizard poisons Spock
            if computer_choice == 3:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 4 and user_input == 0) or (user_input == 4 and computer_choice == 0):
            print(f'Spock smashes scissors.\n')  # Spock smashes Scissors
            if computer_choice == 4:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 0 and user_input == 3) or (user_input == 0 and computer_choice == 3):
            print(f'Scissors decapitate lizard.\n')  # Scissors decapitates Lizard
            if computer_choice == 0:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 3 and user_input == 1) or (user_input == 3 and computer_choice == 1):
            print(f'Lizard eats paper.\n')  # Lizard eats Paper
            if computer_choice == 3:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 1 and user_input == 4) or (user_input == 1 and computer_choice == 4):
            print(f'Paper disproves Spock.\n')  # Paper disproves Spock
            if computer_choice == 1:
                print('Computer wins!')
            else:
                print('You win!')
        elif (computer_choice == 4 and user_input == 2) or (user_input == 4 and computer_choice == 2):
            print(f'Spock vaporizes rock.\n')  # Spock vaporizes Rock
            if computer_choice == 4:
                print('Computer wins!')
            else:
                print('You win!')
        else:
            print(f'Rock crushes scissors.\n')  # Rock crushes Scissors
            if computer_choice == 2:
                print('Computer wins!')
            else:
                print('You win!')

    game()
