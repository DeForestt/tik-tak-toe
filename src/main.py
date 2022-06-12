from os import system
# Python Tik Tak Toe game

board = [ ['-', '-', '-'] ,
          ['-', '-', '-'] ,
          ['-', '-', '-'] ]

# Function to print the board
def print_board(board : list) -> None:
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('---------')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('---------')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

# Function to make a move
def move(x : int, y : int, player : str) -> bool:
    if board[x][y] == '-':
        board[x][y] = player
        return True
    else:
        return False

# A function to check for a win case
def check_win(board : list) -> bool:
    # Check rows
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return True
    # Check columns
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True

# Game loop
def play(board : list) -> None:
    
    for i in range(0, 9):
        print_board(board)
        if i % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        print('Player ' + player + ' turn')

        valid_move = False
        while not valid_move:
            selection = input('Enter x, y: ')
            x, y = selection.split(',')
            x = int(x)
            y = int(y)

            if move(x, y, player):
                valid_move = True
                if check_win(board):
                    print_board(board)
                    print('Player ' + player + ' wins!')
                    return
            else:
                print('Invalid move')
        system('clear')
    print('Game ends in a draw!!!')
    if input('Play again? (y/n): ') == 'y':
        play(board)

play(board)