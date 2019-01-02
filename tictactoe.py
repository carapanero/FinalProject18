class tic_tac_toe:

    def __init__ (self, board, win_combinations):
        self.board = board
        self.win_combinations = win_combinations

    def draw(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()

    def player_one(self):
        not_selected = True
        while not_selected:
            n = int(input("Player 1, chose where to put an X.   "))
            if self.board[n] == "X" or self.board[n] == "O":
                print("That spot is taken. Please pick another location.")
            else:
                self.board[n] = "X"
                not_selected = False

    def player_two(self):
        not_selected = True
        while not_selected:
            n = int(input("Player 2, chose where to put an O.   "))
            if self.board[n] == "X" or self.board[n] == "O":
                print("That spot is taken. Please pick another location.")
            else:
                self.board[n] = "O"
                not_selected = False

game = tic_tac_toe(['0', '1', '2', '3', '4', '5', '6', '7', '8'],[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
game.draw()
game.player_one()
game.draw()
game.player_two()
game.draw()