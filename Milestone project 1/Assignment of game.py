# Tic Tac Toe game in Python

def print_board(board): # This function prints out the board that it was passed
    # "board" is a list of 10 strings representing the board ignore index 0
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
def player_input():# to get input and returns it as (row, col)
    row = 0
    col = 0
    while row not in range(1, 4) or col not in range(1, 4):
        try:
            player_choice = input("Enter the position (row, col) where you want to place your mark (e.g. 1, 2): ")
            row, col = [int(c) for c in player_choice.split(',')]
        except:
            print("Invalid input. Please try again.")
    return (row, col)
def place_marker(board, marker, position): #it places a marker X or O at the desired position on the board  
    board[position] = marker
def win_check(board, marker): # it checks if the given marker has won the game
    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[7] == board[4] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or
            (board[9] == board[6] == board[3] == marker) or
            (board[7] == board[5] == board[3] == marker) or
            (board[9] == board[5] == board[1] == marker))
def board_full(board): # it checks if the board is full and returns a boolean value
    return ' ' not in board[1:]
def play_game():
    print(" Welcome to Tic Tac Toe Game ")
    board = [' '] * 10
    current_player = 'X'
    while True:
        print_board(board)
        print(f"It's {current_player}'s turn.")
        row, col = player_input()
        position = (row-1) * 3 + col
        if board[position] == ' ':
            place_marker(board, current_player, position)
            if win_check(board, current_player):
                print_board(board)
                print(f"{current_player} has won the game!")
                break
            elif board_full(board):
                print_board(board)
                print("The game is a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Please choose a different position.")

if __name__ == '__main__':
    play_game()








