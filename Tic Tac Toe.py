import os
os.system('clear')

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(' {} | {} | {}'.format(self.cells[1], self.cells[2], self.cells[3]))
        print('-----------')
        print(' {} | {} | {}'.format(self.cells[4], self.cells[5], self.cells[6]))
        print('-----------')
        print(' {} | {} | {}'.format(self.cells[7], self.cells[8], self.cells[9]))

    def update_spot(self, cell_no, player):
        if self.cells[cell_no] == ' ':
            self.cells[cell_no] = player

    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True

        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True

        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True

        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True

        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True

        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True

        return False

    def is_tie_game(self):
        used_cells = 0
        for cell in self.cells:
            if cell != ' ':
                used_cells += 1
        if used_cells == 9:
            return True

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()

def print_header():
    print('\nWelcome to Tic Tac Toe!\n')

def refresh_screen():
    # Clear the screen
    os.system('clear')

    # Print the header
    print_header()

    # Show the board
    board.display()

print(refresh_screen())

while True:
    refresh_screen()

    # Get 'X' input
    x_choice = int(input("\nPlease choose where you want to place the 'X' (between 1 - 9): \n"))

    board.update_spot(x_choice, 'X')

    # Refresh screen
    refresh_screen()

    # Check for winner1
    if board.is_winner('X') == True:
        print('\nX Wins!\n')
        play_again = input('\nWould you like to play again? (Y/N): \n').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            print('\nThanks for playing!\n')
            break

    # Check for a tie
    if board.is_tie_game():
        print('Tie game! ')
        play_again = input('\nWould you like to play again? (Y/N): \n').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            print('\nThanks for playing!\n')
            break

    # Get 'O' input
    o_choice = int(input("\nPlease choose where you want to place the 'O' (between 1 - 9): \n"))

    board.update_spot(o_choice, 'O')

    if board.is_winner('O') == True:
        print('\nO Wins!\n')
        play_again = input('\nWould you like to play again? (Y/N): \n').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            print('\nThanks for playing! ')
            break

    # Check for a tie
    if board.is_tie_game():
        print('\nTie game!\n')
        play_again = input('\nWould you like to play again? (Y/N): \n').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            print('\nThanks for playing! ')
            break
