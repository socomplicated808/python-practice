import os

class Board:
    
    def __init__(self):
        self.squares = ["[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]"]
        self.draw_board()

    
    def draw_board(self):
        clearConsole = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')
        clearConsole()
        print(f"{self.squares[0]} | {self.squares[1]} | {self.squares[2]}")
        print("----|-----|----")
        print(f"{self.squares[3]} | {self.squares[4]} | {self.squares[5]}")
        print("----|-----|----")
        print(f"{self.squares[6]} | {self.squares[7]} | {self.squares[8]}")


    def check_win(self,mark):
        win = False
        if self.squares[0] == mark and self.squares[1] == mark and self.squares[2] == mark:
            win = True
        elif self.squares[3] == mark and self.squares[4] == mark and self.squares[5] == mark:
            win = True
        elif self.squares[6] == mark and self.squares[7] == mark and self.squares[8] == mark:
            win = True
        elif self.squares[0] == mark and self.squares[4] == mark and self.squares[8] == mark:
            win = True
        elif self.squares[2] == mark and self.squares[4] == mark and self.squares[6] == mark:
            win = True
        elif self.squares[0] == mark and self.squares[3] == mark and self.squares[6] == mark:
            win = True
        elif self.squares[1] == mark and self.squares[4] == mark and self.squares[7] == mark:
            win = True
        elif self.squares[2] == mark and self.squares[5] == mark and self.squares[8] == mark:
            win = True
        return win





