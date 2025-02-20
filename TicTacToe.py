from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.YELLOW + "\nLet's Start Playing Tic-Tac-Toe Game:" + Fore.YELLOW + '\n')
name1 = input(Back.WHITE + Style.BRIGHT + ' Enter - Player 1 NAME: ' + Style.RESET_ALL + Back.RESET + '\n>> ')
name2 = input(Back.WHITE + Style.BRIGHT +' Enter -  Player 2 NAME: ' + Style.RESET_ALL + Back.RESET + '\n>> ')

player_symbol = input(Fore.CYAN + "\nEnter Player 1 symbol: 'X' or 'O' \n" + Fore.RESET + ">> ").upper()
while player_symbol not in ['X', 'O']:
    print(Fore.RED + "\nInvalid input! Enter 'X' or 'O'" + Fore.RESET)
    player_symbol = input(Fore.CYAN + "\nEnter your symbol 'X' or 'O'" + Fore.RESET + ">> ").upper()
if player_symbol == 'X':
    player1 = Fore.MAGENTA + 'X' + Fore.RESET
    player2 = Fore.YELLOW + 'O' + Fore.RESET
else:
    player1 = Fore.MAGENTA + 'O' + Fore.RESET
    player2 = Fore.YELLOW + 'X' + Fore.RESET
print(Back.WHITE + Style.BRIGHT + f" Player 1| {name1} - {player1} " + Style.RESET_ALL + Back.RESET)
print(Back.WHITE + Style.BRIGHT + f" Player 2| {name2} - {player2} " + Style.RESET_ALL + Back.RESET)
board = [' ' for _ in range(9)]
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

for turn in range(9):
    print_board()
    current_player = player1 if turn%2==0 else player2
    if current_player is player1:
        name = Fore.MAGENTA + name1 + Fore.RESET
    else:
        name = Fore.YELLOW + name2 + Fore.RESET
    move = int(input('\n' + Fore.BLUE + f'Player {name}| {current_player} - Enter your move (1-9)' + Fore.RESET + '\n>> '))-1
    if 0 <= move < 9 and board[move] == ' ':
        board[move] = current_player
    else:
        print(Fore.RED + '\nInvalid move! Try again.\n' + Fore.RESET)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [2, 4, 6], [0, 4, 8]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            print_board()
            print(Fore.GREEN + f'\nPlayer {name} Wins! Congratulations.\nThanks for Playing!' + Fore.RESET + '\n')
            exit()
print_board()
print(Back.YELLOW + "It's a draw! 🙃 \n" + Back.RESET)