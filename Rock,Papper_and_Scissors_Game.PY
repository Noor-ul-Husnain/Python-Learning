from tkinter import *
import random

player_score = 0
computer_score = 0

def gamewin(computer, player):
    if computer == player:
        return "It is a tie."
    elif (computer == 'r' and player == 's') or (computer == 'p' and player == 'r') or (computer == 's' and player == 'p'):
        return True
    else:
        return False

print('''Hello!
  Today we are playing Rock, Paper, Scissors game.
To win you have to score 10 points before the computer.
\t\tLet's begin!
''')

def click(button_number):
    player_choice = None
    if button_number == 1:
        player_choice = 'r'
    elif button_number == 2:
        player_choice = 'p'
    elif button_number == 3:
        player_choice = 's'
    play_game(player_choice)

def play_game(player_choice):
    global player_score, computer_score

    if player_choice not in ['r', 'p', 's']:
        print("This is not valid.")
    else:
        print("OK! The computer is choosing...")
        compturn = random.randint(1, 3)
        if compturn == 1:
            computer = 'r'
        elif compturn == 2:
            computer = 'p'
        elif compturn == 3:
            computer = 's'

        print("YOU: " + player_choice + " , COMPUTER: " + computer)

        result = gamewin(computer, player_choice)
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

window = Tk()
rock = PhotoImage(file='Rock.png')
papper = PhotoImage(file='paper.png')
scissor = PhotoImage(file='scissor.png')
re_sized = rock.subsample(7, 9)
re_sized2 = papper.subsample(7, 9)
re_sized3 = scissor.subsample(7, 9)

button1 = Button(window, 
                 command=lambda: click(1), 
                 image=re_sized)
button2 = Button(window, 
                command=lambda: click(2), 
                image=re_sized2)
button3 = Button(window, 
                command=lambda: click(3), 
                image=re_sized3)

button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

window.mainloop()
# Test Commit