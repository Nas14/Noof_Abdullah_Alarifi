# Problem 6: Rock, Paper, Scissors
# --------------------------------
# Ask two players to enter their choice: "rock", "paper", or
# "scissors". Print the result:
#   - "Tie"            if both chose the same
#   - "Player 1 wins"  if Player 1 beats Player 2
#   - "Player 2 wins"  otherwise
 
# Game rules:
#   - rock      beats  scissors
#   - scissors  beats  paper
#   - paper     beats  rock
 
# Constraint: NO logical operators. Use if-elif-else with nested
# if-else inside each branch.

player1 = input ("Enter Your Choice (rock, paper, scissors), Player 1: ")
player2 = input ("Enter Your Choice (rock, paper, scissors), Player 2: ")


if player1 == player2:
    print ("Tie")
elif player1 == "rock":
    if player2 == "scissors":
         print ("Player 1 wins")
    else:
         print ("Player 2 wins")
elif player1 == "scissors":
    if player2 == "paper":
         print ("Player 1 wins")
    else:
         print ("Player 2 wins")
elif player1 == "paper":
    if player2 == "rock":
         print ("Player 1 wins")
    else:
         print ("Player 2 wins")    