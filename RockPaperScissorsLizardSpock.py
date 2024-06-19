#This program produces a random number for the game rock paper scissors lizard Spock to refrence.  
import random

#All of the options
options = ("rock", "paper", "scissors", "lizard", "spock" )
playing = True

#This is the main loop where things happen
while playing:
    print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock! \nPlease select an option to play: \n- Rock \n- Paper \n- Scissors \n- Lizard \n- Spock ')
    computer = random.choice(options)
    user = input('Your choice:  ').lower()
    while user not in options:
        user = input("Enter one of the following:  \n- Rock \n- Paper \n- Scissors \n- Lizard \n- Spock \n Choice:  ").lower()
    
    #Results of contest
    print(f'\nYou chose {user} and the opponent chose {computer}!')
    if user == computer:
        print('You have tied!')
    elif user == "rock" and computer == "lizard":
        print('Rock crushes Lizard!')
        print('You Win!')
    elif user == "rock" and computer == "scissors":
        print('Rock destroys Scissors!')
        print('You Win!')
    elif user == "paper" and computer == "spock":
        print('Paper disproves Spock!')
        print('You Win!')
    elif user == "paper" and computer == "rock":
        print('Paper covers Rock!')
        print('You Win!')
    elif user == "scissors" and computer == "paper":
        print('Scissors cuts Paper!')
        print('You Win!')
    elif user == "scissors" and computer == "lizard":
        print('Scissors decapitates Lizard!')
        print('You Win!')
    elif user == "lizard" and computer == "paper":
        print('Lizard eats Paper!')
        print('You Win!')
    elif user == "lizard" and computer == "spock":
        print('Lizard poisons Spock!')
        print('You Win!')
    elif user == "spock" and computer == "scissors":
        print('Spock smashes Scissors!')
        print('You Win!')
    elif user == "spock" and computer == "rock":
        print('Spock vaporizes Rock!')
        print('You Win!')
    elif computer == "rock" and user == "lizard":
        print('Rock crushes Lizard!')
        print('You Lose!')
    elif computer == "rock" and user == "scissors":
        print('Rock destroys Scissors!')
        print('You Lose!')
    elif computer == "paper" and user == "spock":
        print('Paper disproves Spock!')
        print('You Lose!')
    elif computer == "paper" and user == "rock":
        print('Paper covers Rock!')
        print('You Lose!')
    elif computer == "scissors" and user == "paper":
        print('Scissors cuts Paper!')
        print('You Lose!')
    elif computer == "scissors" and user == "lizard":
        print('Scissors decapitates Lizard!')
        print('You Lose!')
    elif computer == "lizard" and user == "paper":
        print('Lizard eats Paper!')
        print('You Lose!')
    elif computer == "lizard" and user == "spock":
        print('Lizard poisons Spock!')
        print('You Lose!')
    elif computer == "spock" and user == "scissors":
        print('Spock smashes Scissors!')
        print('You Lose!')
    elif computer == "spock" and user == "rock":
        print('Spock vaporizes Rock!')
        print('You Lose!')
    else:
        print('What is your quest?  ')              #This line is for debugging, it will let me know if there is an unmatched set or a larger issue if displayed.
        
    #Continue or quit
    quit = input('\nDo you want to play again? type Yes or No:  ').lower()       #User must enter Yes(y) or No(n) to continue
    options2 = ("y", "yes", "n", "no")
    while quit not in options2:
        quit = input(f'{quit} was not a valid option! \nDo you want to play again? \nType Yes or No! \nAnswer:  ')
    if quit == "y" or quit == "yes":
        continue
    elif quit == "n" or quit == "no":
        break
    else:
        print('Ni')             #A option to see if the code is running properly
    