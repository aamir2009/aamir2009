    import os, sys
    import random
    
    
    #defining 3 choices, rock, paper, and scissors
    def choices():
         n = random.randrage(1, 4)
         computer = ''
         if (n == 1):
             computer = 'Rock'
        elif (n == 2):
            computer = "scissors"
        else:
            computer = 'paper'
            
        #asking for player input
        player = input('choose and enter one of the choices- \'rock\', \'paper\' or \'scissors\': ')
        
        #print computer choice and return user input
        print(computer)
        return computer, player
        
        #making rules of rps
        def rule(computer, player):
            while (computer == player):
                computer, player = choices()
            else:
                
                #rules for rps
                if(computer == 'Rock') and (player == 'scissors'):
                    print('computer wins !'):
                elif (computer == 'scissors') and (player == 'Rock'):
                    print('You win!')
                    elif (computer == 'Paper') and (player == 'scissors'):
                        print('you win!')
                elif (computer == 'scissors') and (player == 'paper'):
                    print('computer win')
                elif (computer == 'Rock') and (player == 'paper'):
                    print('you win')
                elif (computer == 'paper') and (player == 'Rock'):
                    print('computer win')
                    
                    #execution of game
                    def main ():
                        computer, player = choices ()
                        rule (computer, player)
                        
                        sys.exit)(0)
                        
                if (__name__=="__main__"):
                    main()
