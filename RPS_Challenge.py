# Rock, Paper, Scissor Game: A fun interactive game where the player competes against the computer.

import random

# Greet the user
name = input("What's your name: ")
print(f"Hi, {name}! Nice to see you here. Let's play rock, paper, scissor game now.")

# Initialize score variables
wins = 0
losses = 0
ties = 0

def play_game(player_move):
    global wins, losses, ties  

    randomNumber = random.randint(1, 3)
    computer_move = ''
    
    if randomNumber == 1:
        computer_move = 'ROCK'
    elif randomNumber == 2:
        computer_move = 'PAPER'
    elif randomNumber == 3:
        computer_move = 'SCISSOR'

    print(f"Computer chose: {computer_move}")

    # Determine the game result
    if player_move == 'r' and randomNumber == 1 or \
       player_move == 'p' and randomNumber == 2 or \
       player_move == 's' and randomNumber == 3:
        print('It\'s a Tie!')
        ties += 1
    elif player_move == 'r' and randomNumber == 2:
        print('ROCK versus PAPER - PAPER Wins. You Lose!')
        losses += 1
    elif player_move == 'r' and randomNumber == 3:
        print('ROCK versus SCISSOR - ROCK Wins. You WON!')
        wins += 1
    elif player_move == 'p' and randomNumber == 1:
        print('PAPER versus ROCK - PAPER Wins. You WON!')
        wins += 1
    elif player_move == 'p' and randomNumber == 3:
        print('PAPER versus SCISSOR - SCISSOR Wins. You Lose!')
        losses += 1
    elif player_move == 's' and randomNumber == 1:
        print('SCISSOR versus ROCK - ROCK Wins. You Lose!')
        losses += 1
    elif player_move == 's' and randomNumber == 2:
        print('SCISSOR versus PAPER - SCISSOR Wins. You WON!') 
        wins += 1

# Game loop
while True:
    print('\n(r)ock, (p)aper, (s)cissors, (q)uit')
    player_move = input("Enter your move : ").lower()

    if player_move == 'q':
        print(f'Well played {name}! Final Score:')
        print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')
        print('See you soon!')
        break
    elif player_move in ['r', 'p', 's']:
        play_game(player_move)
    else:
        print('Invalid input. Please enter r, p, s, or q.')

#Thank you for Playing!









