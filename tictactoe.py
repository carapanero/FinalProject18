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

game = tic_tac_toe(['1', '2', '3', '4', '5', '6', '7', '8', '9'],[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
game.draw()