#create a class for tic-tac-toe and initialize variables
class tic_tac_toe:
    def __init__ (self, board, win_combos):
        self.board = board
        self.win_combos = win_combos
#show no one has won the game yet
        self.victory = False
#define a function to draw the game board
    def draw(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()
#define a function for player one's turn
    def player_one(self):
        not_selected = True
        numbers = [0,1,2,3,4,5,6,7,8]
        while not_selected:
            try:
                n = int(input("Player 1, chose where to put an X."))
                if n in numbers:
                    if self.board[n] == "X" or self.board[n] == "O":
                        print("That spot is taken. Please pick another location.")
                    else:
                        self.board[n] = "X"
                        not_selected = False
            except:
                print("Please enter a valid option")
#define a function for player two's turn
    def player_two(self):
        not_selected = True
        numbers = [0,1,2,3,4,5,6,7,8]
        while not_selected:
            try:
                n = int(input("Player 2, chose where to put an X."))
                if n in numbers:
                    if self.board[n] == "O" or self.board[n] == "O":
                        print("That spot is taken. Please pick another location.")
                    else:
                        self.board[n] = "O"
                        not_selected = False
            except:
                print("Please enter a valid option.")
#define a function to see if someone has won the game
    def check_win(self, player):
        for combo in self.win_combos:
            win = True
            for pos in combo:
                if self.board[pos] != player:
                    win = False
            if win:
                self.victory = True
                print("Winner! Game over.")
            if self.victory == False and all(x.isalpha() for x in self.board):
                print("You tie. Game over.")
                self.victory = True

#classify game as tic-tac-toe and provide conditions
game = tic_tac_toe(['0', '1', '2', '3', '4', '5', '6', '7', '8'],[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
#print a welcome statement
print("Time to play tic-tac-toe!")
#draw the board
game.draw()
#create a loop for game play that ends when someone wins
while not game.victory:
    game.player_one()
    game.draw()
    game.check_win("X")
    if game.victory == True:
        break
    game.player_two()
    game.draw()
    game.check_win("O")

