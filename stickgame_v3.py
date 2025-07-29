from random import randint

name = input("What is your name: ") 
print("Hi "+ name +" Welcome to Who take the last stick lose! Game!") 
print("You can pick stick out from pile atleast 1 and no more than 4") 
print("The first player will be randome picked. Enjoy the game!!!")
# Set up variable to store name from user. Make the welcome message to player

player_count = 0 
python_count = 0 
# Set variable to count guess number from two player

stick_in_pile = randint(6,100)
# Set up random number for stick in pile


def python_turn():
# Define function for python turn

    global stick_in_pile
    global python_count
    # Define global variable to use in this function and also update information in order to find a winner later

    target_number = [i for i in range(6, stick_in_pile+1) if i % 5 == 1]
    x = stick_in_pile
    a = randint(1,4)   
    # Set up local variable to use in this function for target will use to make a strategy for python turn.
    # x to check the number stick in pile, and use as reference for checking below condition

    while x-a not in target_number and x > 5:
      a = randint(1,4)
      # make loop to make python pick any within the list above. Garanty win for sure

    if 1 < x <=5 :
      a = x-1
      # incase a number below than 5 making python to pick the minus 1 of stick in the pile. This will make a stick only one left in pile

    python_pick = a
    stick_in_pile -= python_pick
    # Update value of the stick in pile

    python_count += 1
    # Count turn for calculate winner later

def player_turn():
# Define function for player turn

    global stick_in_pile
    global player_count
    # Define global variable to use in this function and also update information in order to find a winner later

    player_pick = 0
    # Set up variable to make while loop

    while player_pick < 1 or player_pick > 4:
    # Start loop due to player_pick align with the rule

        if stick_in_pile <= 1 :
            break
            # To check wether stick left in the pile. If there are sticks left in pile, this program will allow player to put desired number

        player_pick = int(input("Please enter the number of stick to take out: "))
        # Making player put the number with below condition

        if player_pick < 1:
            print("No, you cannot take less than 1 stick!")
            # making condition to check if the input number is not lower or equal to 0. a function will ask player a again if input number meet this condition

        elif player_pick > 4 :
            print("No, you cannot take more than 2 sticks!")
            # making conditon to check if the input number is not higher than 4. a function will ask player again if input number meet this condition
        
        elif stick_in_pile - player_pick < 0:
            print("There are no enough sticks to take")
            # Making condition to check if input number of stick is higher than stick which is lefted over in plie. the function will ask player to input numner again
        
        else:
            stick_in_pile -= player_pick
            player_count += 1
            # making a conditon if the input number meet a requirement (1 to 4). A stick in pile will be detucted by the player's input number.

while stick_in_pile > 1 :
# Starting game by checking the number in pile first. if it more than one, a game will start.
    if stick_in_pile <= 1: 
        break
        # If next turn will only have one left. A game will automatically stop and will anonce the winner.

    elif stick_in_pile % 5 == 1 : 
        print("Hey "+name+" Please take out the stick:") 
        player_turn() 
        python_turn() 
        print("There are ", stick_in_pile ," left in a pile")
        # to make AI alway win this game if the number of stick at the beginning align with this condition player will start first
        
    else : 
         python_turn() 
         print("There are ", stick_in_pile ," left in a pile") 
         player_turn()
         # On the other hand, if the starting number is not follow the rule. The game will start by python to make the next number align with the target_number at the top

if player_count <  python_count: 
    print("You lose, try again next time")
    # if the game stop and any player with have lower count, they will be loser.
    
else: 
    print("Congratulation, You win")
