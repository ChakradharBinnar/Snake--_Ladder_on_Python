import random

print("\nWelcome in Snake And Ladder\n")

player1 = input("Enter player-1 name : ")
player2 = input("Enter player-2 name : ")
print("\n")

Board_Size = 100
player1_pos = 0
player2_pos = 0

snake = {16: 6, 25 :5, 40:7, 55:22, 60:40, 75:44, 82:48, 94:2}
ladder = {3: 22, 9 :30, 32:66, 40:59, 62:77, 80:95}

def move (position):
    Throw_Dice = random.randint(1, 6)
    print(f"You got: {Throw_Dice}")
    position = Throw_Dice + position

    if position in snake:
        print(f"Snake Bite you at position: {position}")
        position = snake[position]
        print(f"Go back at {position} position.")
   
    elif position in ladder:
        print(f"You got the ladder at position: {position}")
        position = ladder[position]
        print(f"climb ladder & go forward at position: {position}")
   
    else:
        print(f"Your Current position is: {position}")

    print("\n")
    return position
    


while True:
    input(f"Its {player1} turn for throw the dice. plzz press enter to throw dice ! ")
    player1_pos = move(player1_pos)

    if (player1_pos > Board_Size):
        print(f"Congratulations {player1} ! You Won the Game \n")
        break

    input(f"Its {player2} turn for throw the dice. plzz press enter to throw dice ! ")
    player2_pos = move(player2_pos)

    if (player2_pos > Board_Size):
        print(f"Congratulations {player2} ! You Won the Game \n")
        break