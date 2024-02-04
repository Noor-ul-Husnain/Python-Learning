player_score = 0
computer_score = 0

print('''Hello!
  Today we are playing Rock, Paper, Scissors game.
To win you have to score 10 points before the computer.
\t\tLet's begin!
''')

while (player_score < 10) and (computer_score < 10):
    player = input('''Choose: Rock(r), Paper(p) or Scissors(s)\n''').lower()

    if player not in ['r', 'p', 's']:
        print("This is not valid.")
    else:
        print("OK! The computer is choosing...")
        import random
        compturn = random.randint(1, 3)
        if compturn == 1:
            computer = 'r'
        elif compturn == 2:
            computer = 'p'
        elif compturn == 3:
            computer = 's'

        def gamewin(computer, player):
            if computer == player:
                return "It is a tie."
            elif (computer == 'r' and player == 's') or (computer == 'p' and player == 'r') or (computer == 's' and player == 'p'):
                return True
            else:
                return False

        print("YOU: " + player + " , COMPUTER: " + computer)

        result = gamewin(computer, player)
        if result is True:
            computer_score += 1
            if computer_score == 10:
                print("You Lose!")
        elif result is False:
            player_score += 1
            if player_score == 10:
                print("You Win!")
        else:
            print(result)

        print(f"Score of computer: {computer_score}")
        print(f"Score of player: {player_score}")
