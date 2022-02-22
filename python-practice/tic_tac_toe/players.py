import os


class Player:

    def __init__(self,mark):
        self.mark = mark

    def put_mark(self,mark,board_object):
        '''Returns an integer representing the space for the X or O goes'''

        while True:
            number = input(f"Player {mark}, Enter the number where you want to place an {mark}: ")

            #Continually asks the user for input until an integer is input
            try:
                if isinstance(int(number),int):
                    break
            except ValueError:
                clearConsole = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')
                clearConsole()
                board_object.draw_board()
                print("That is not a number. Please input a number.")

        return int(number)