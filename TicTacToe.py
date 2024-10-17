# Tic Tac Toe Game
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Get Player 1's symbol
player1_symbol = input(Fore.CYAN + "Player 1 - choose your symbol (X or O) 😊 : ").upper()


while player1_symbol not in ["X", "O"]:
    print(Fore.RED + "Invalid choice! 🫡  Please select X or O" + Fore.RESET)
    player1_symbol = input(Fore.CYAN + "Player 1 - choose your symbol (X or O) 😊 : ").upper()

if player1_symbol == "X":
    player1 = Fore.MAGENTA + "X" + Fore.RESET
    player2 = Fore.YELLOW + "O" + Fore.RESET
else:
    player1 = Fore.MAGENTA + "O" + Fore.RESET
    player2 = Fore.YELLOW + "X" + Fore.RESET


print(Back.MAGENTA + f"Player 1 - '{player1}' | Player 2 - '{player2}'." + Back.RESET)


the_board = [' ' for _ in range(9)]


def print_board():
    print(the_board[0] + '|' + the_board[1] + '|' + the_board[2])
    print('-+-+-')
    print(the_board[3] + '|' + the_board[4] + '|' + the_board[5])
    print('-+-+-')
    print(the_board[6] + '|' + the_board[7] + '|' + the_board[8])

# Main game loop
for turn in range(9):
    print('\n')
    print_board()
    current_player = player1 if turn % 2 == 0 else player2
    move = int(input(Fore.CYAN + f"Player {current_player} 😀 - Enter your move (1-9) >>  ")) - 1

    # Check for valid move
    if 0 <= move < 9 and the_board[move] == ' ':
        the_board[move] = current_player
    else:
        print(Fore.RED + "Invalid move! Try again." + Fore.RESET)
        continue

    # Check for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if the_board[condition[0]] == the_board[condition[1]] == the_board[condition[2]] != ' ':
            print('\n')
            print_board()
            print(Fore.GREEN + f"🥳 Player {current_player} wins! 😃😍" + Fore.RESET)
            exit()


print_board()
print(Back.YELLOW + "It's a draw! 🙃" + Back.RESET)


