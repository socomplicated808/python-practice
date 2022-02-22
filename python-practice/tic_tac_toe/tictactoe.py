from board import Board
from players import Player

board = Board()
player_x = Player(" X ")
player_y = Player(" O ")
current_player = player_x
game = True

while game:
    square_number = current_player.put_mark(current_player.mark,board)
    board.squares[square_number] = current_player.mark
    board.draw_board()
    if board.check_win(current_player.mark):
        print(f"Player {current_player.mark} wins!!!")
        game = False
    if current_player == player_x:
        current_player = player_y
    elif current_player == player_y:
        current_player = player_x