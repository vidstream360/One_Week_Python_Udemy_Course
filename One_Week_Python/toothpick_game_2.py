#pick up sticks game
#ask for player names

#Game loop, until someone wins
#limit player to 1, 2 or 3 takes
#ask player to enter number
#check to see if they win

#ask player2 to enter number
#check to see if they win

print("Welcome To The Game!")
print("********************")
num_left = 13
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
current_player = player1_name

while True:
    print("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"{current_player}, how many toothpicks do you take? "))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input(f"You can only chose 1, 2, or 3: "))
    num_left -= choice
    if num_left <= 0:
        print(f"{current_player} wins the game!")
        break
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name

print("GAME OVER!")
