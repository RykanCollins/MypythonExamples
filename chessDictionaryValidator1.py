def isValidChessBoard(board_dict):

# exactly one black king and exactly one white king
    if ('bking' or 'wking') not in board_dict.values():
        return False

# each player can only have at most 16 pieces
    w_color_num = b_color_num = 0
    for v in board_dict.values():
        if v[0] == 'b':
            b_color_num = b_color_num + 1
        elif v[0] == 'w':
            w_color_num = w_color_num + 1
        if (w_color_num or b_color_num) > 16:
            return False
    #print(b_color_num)

# at most 8 pawns
    new_board_dict = {}
    for v in board_dict.values():
        new_board_dict.setdefault(v,0)
        new_board_dict[v] = new_board_dict[v] + 1
    #print(new_board_dict)

    for x in ['bpawn', 'wpawn']:
        if x in new_board_dict.keys():
            if new_board_dict[x] not in range(9):
                return False

# valid space from '1a' to '8h'
    for location in board_dict.keys():
        row = int(location[0])
        column = location[-1]
        if not ((row in range(1, 9)) and ('a' <= column <= 'h')):
            return False

# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
    pieces = ['king','queen','rook', 'knight','bishop','knight', 'pawn']
    colors = ['b', 'w']
    all_pieces = set()
    for p in pieces: # shortcut: all_pieces = set(color+piece for piece in pieces for color in colors)
        for c in colors:
            #print(c+p)
            all_pieces.add(c+p)
    #print(type(all_pieces))
    #print(all_pieces)
    for v in board_dict.values():
        if v not in all_pieces:
            return False
            
# This function should detect when a bug has resulted in an improper chess board.

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))
