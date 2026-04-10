import pygame
import chess
import chess.engine
from sys import exit

pygame.init()

while True:
    side = input("Do You want to play as white or black? press 'w' for white, 'b' for black: ")
    if side == 'w':
        print("You have choosen to play as white.")
        break
    elif side == 'b':
        print("You have choosen to play as black.")
        break
    print("please enter either 'w' or 'b' for white or black, anything other than that is unacceptable.")

while True:
    diff = input("Choose Stockfish difficulty (1-20): ")
    if diff.isdigit() and 1 <= int(diff) <= 20:
        difficulty = int(diff)
        print(f"Difficulty set to {difficulty}.")
        break
    print("Please enter a number between 1 and 20.")

engine = chess.engine.SimpleEngine.popen_uci(
    r"C:\Users\Muhammad Ali\PyCharmMiscProject\stockfish\stockfish-windows-x86-64-avx2.exe")
engine.configure({"Skill Level": difficulty})

board = chess.Board()

# Row 8
a8 = pygame.Rect(71, 71, 70, 70)
b8 = pygame.Rect(141, 71, 70, 70)
c8 = pygame.Rect(211, 71, 70, 70)
d8 = pygame.Rect(281, 71, 70, 70)
e8 = pygame.Rect(351, 71, 70, 70)
f8 = pygame.Rect(421, 71, 70, 70)
g8 = pygame.Rect(491, 71, 70, 70)
h8 = pygame.Rect(561, 71, 70, 70)

# Row 7
a7 = pygame.Rect(71, 141, 70, 70)
b7 = pygame.Rect(141, 141, 70, 70)
c7 = pygame.Rect(211, 141, 70, 70)
d7 = pygame.Rect(281, 141, 70, 70)
e7 = pygame.Rect(351, 141, 70, 70)
f7 = pygame.Rect(421, 141, 70, 70)
g7 = pygame.Rect(491, 141, 70, 70)
h7 = pygame.Rect(561, 141, 70, 70)

# Row 6
a6 = pygame.Rect(71, 211, 70, 70)
b6 = pygame.Rect(141, 211, 70, 70)
c6 = pygame.Rect(211, 211, 70, 70)
d6 = pygame.Rect(281, 211, 70, 70)
e6 = pygame.Rect(351, 211, 70, 70)
f6 = pygame.Rect(421, 211, 70, 70)
g6 = pygame.Rect(491, 211, 70, 70)
h6 = pygame.Rect(561, 211, 70, 70)

# Row 5
a5 = pygame.Rect(71, 281, 70, 70)
b5 = pygame.Rect(141, 281, 70, 70)
c5 = pygame.Rect(211, 281, 70, 70)
d5 = pygame.Rect(281, 281, 70, 70)
e5 = pygame.Rect(351, 281, 70, 70)
f5 = pygame.Rect(421, 281, 70, 70)
g5 = pygame.Rect(491, 281, 70, 70)
h5 = pygame.Rect(561, 281, 70, 70)

# Row 4
a4 = pygame.Rect(71, 351, 70, 70)
b4 = pygame.Rect(141, 351, 70, 70)
c4 = pygame.Rect(211, 351, 70, 70)
d4 = pygame.Rect(281, 351, 70, 70)
e4 = pygame.Rect(351, 351, 70, 70)
f4 = pygame.Rect(421, 351, 70, 70)
g4 = pygame.Rect(491, 351, 70, 70)
h4 = pygame.Rect(561, 351, 70, 70)

# Row 3
a3 = pygame.Rect(71, 421, 70, 70)
b3 = pygame.Rect(141, 421, 70, 70)
c3 = pygame.Rect(211, 421, 70, 70)
d3 = pygame.Rect(281, 421, 70, 70)
e3 = pygame.Rect(351, 421, 70, 70)
f3 = pygame.Rect(421, 421, 70, 70)
g3 = pygame.Rect(491, 421, 70, 70)
h3 = pygame.Rect(561, 421, 70, 70)

# Row 2
a2 = pygame.Rect(71, 491, 70, 70)
b2 = pygame.Rect(141, 491, 70, 70)
c2 = pygame.Rect(211, 491, 70, 70)
d2 = pygame.Rect(281, 491, 70, 70)
e2 = pygame.Rect(351, 491, 70, 70)
f2 = pygame.Rect(421, 491, 70, 70)
g2 = pygame.Rect(491, 491, 70, 70)
h2 = pygame.Rect(561, 491, 70, 70)

# Row 1
a1 = pygame.Rect(71, 561, 70, 70)
b1 = pygame.Rect(141, 561, 70, 70)
c1 = pygame.Rect(211, 561, 70, 70)
d1 = pygame.Rect(281, 561, 70, 70)
e1 = pygame.Rect(351, 561, 70, 70)
f1 = pygame.Rect(421, 561, 70, 70)
g1 = pygame.Rect(491, 561, 70, 70)
h1 = pygame.Rect(561, 561, 70, 70)

squares = {
    "a1": a1, "b1": b1, "c1": c1, "d1": d1, "e1": e1, "f1": f1, "g1": g1, "h1": h1,
    "a2": a2, "b2": b2, "c2": c2, "d2": d2, "e2": e2, "f2": f2, "g2": g2, "h2": h2,
    "a3": a3, "b3": b3, "c3": c3, "d3": d3, "e3": e3, "f3": f3, "g3": g3, "h3": h3,
    "a4": a4, "b4": b4, "c4": c4, "d4": d4, "e4": e4, "f4": f4, "g4": g4, "h4": h4,
    "a5": a5, "b5": b5, "c5": c5, "d5": d5, "e5": e5, "f5": f5, "g5": g5, "h5": h5,
    "a6": a6, "b6": b6, "c6": c6, "d6": d6, "e6": e6, "f6": f6, "g6": g6, "h6": h6,
    "a7": a7, "b7": b7, "c7": c7, "d7": d7, "e7": e7, "f7": f7, "g7": g7, "h7": h7,
    "a8": a8, "b8": b8, "c8": c8, "d8": d8, "e8": e8, "f8": f8, "g8": g8, "h8": h8,
}

window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load(r"png\chess.png"))

canvas = pygame.Surface((700, 700))

Chessboard = pygame.image.load(r'png\chessboard.png').convert_alpha()
Chessboard = pygame.transform.scale(Chessboard, (700, 700))

def load(path):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (70, 70))

def load_flipped(path):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (70, 70))
    return pygame.transform.rotate(img, 180)

# Each piece gets its own fresh surface load — no shared references
ldr = load_flipped if side == 'b' else load

white_king    = ldr(r'png\white_king.png')
white_queen   = ldr(r'png\white_queen.png')
white_rook1   = ldr(r'png\white_rook.png')
white_rook2   = ldr(r'png\white_rook.png')
white_bishop1 = ldr(r'png\white_bishop.png')
white_bishop2 = ldr(r'png\white_bishop.png')
white_knight1 = ldr(r'png\white_knight.png')
white_knight2 = ldr(r'png\white_knight.png')
white_pawn1   = ldr(r'png\white_pawn.png')
white_pawn2   = ldr(r'png\white_pawn.png')
white_pawn3   = ldr(r'png\white_pawn.png')
white_pawn4   = ldr(r'png\white_pawn.png')
white_pawn5   = ldr(r'png\white_pawn.png')
white_pawn6   = ldr(r'png\white_pawn.png')
white_pawn7   = ldr(r'png\white_pawn.png')
white_pawn8   = ldr(r'png\white_pawn.png')

black_king    = ldr(r'png\black_king.png')
black_queen   = ldr(r'png\black_queen.png')
black_rook1   = ldr(r'png\black_rook.png')
black_rook2   = ldr(r'png\black_rook.png')
black_bishop1 = ldr(r'png\black_bishop.png')
black_bishop2 = ldr(r'png\black_bishop.png')
black_knight1 = ldr(r'png\black_knight.png')
black_knight2 = ldr(r'png\black_knight.png')
black_pawn1   = ldr(r'png\black_pawn.png')
black_pawn2   = ldr(r'png\black_pawn.png')
black_pawn3   = ldr(r'png\black_pawn.png')
black_pawn4   = ldr(r'png\black_pawn.png')
black_pawn5   = ldr(r'png\black_pawn.png')
black_pawn6   = ldr(r'png\black_pawn.png')
black_pawn7   = ldr(r'png\black_pawn.png')
black_pawn8   = ldr(r'png\black_pawn.png')

white_king_rect    = white_king.get_rect(topleft=(351, 561))
white_queen_rect   = white_queen.get_rect(topleft=(281, 561))
white_rook1_rect   = white_rook1.get_rect(topleft=(71, 561))
white_rook2_rect   = white_rook2.get_rect(topleft=(561, 561))
white_bishop1_rect = white_bishop1.get_rect(topleft=(211, 561))
white_bishop2_rect = white_bishop2.get_rect(topleft=(421, 561))
white_knight1_rect = white_knight1.get_rect(topleft=(141, 561))
white_knight2_rect = white_knight2.get_rect(topleft=(491, 561))
white_pawn1_rect   = white_pawn1.get_rect(topleft=(71, 491))
white_pawn2_rect   = white_pawn2.get_rect(topleft=(141, 491))
white_pawn3_rect   = white_pawn3.get_rect(topleft=(211, 491))
white_pawn4_rect   = white_pawn4.get_rect(topleft=(281, 491))
white_pawn5_rect   = white_pawn5.get_rect(topleft=(351, 491))
white_pawn6_rect   = white_pawn6.get_rect(topleft=(421, 491))
white_pawn7_rect   = white_pawn7.get_rect(topleft=(491, 491))
white_pawn8_rect   = white_pawn8.get_rect(topleft=(561, 491))

black_king_rect    = black_king.get_rect(topleft=(351, 71))
black_queen_rect   = black_queen.get_rect(topleft=(281, 71))
black_rook1_rect   = black_rook1.get_rect(topleft=(71, 71))
black_rook2_rect   = black_rook2.get_rect(topleft=(561, 71))
black_bishop1_rect = black_bishop1.get_rect(topleft=(211, 71))
black_bishop2_rect = black_bishop2.get_rect(topleft=(421, 71))
black_knight1_rect = black_knight1.get_rect(topleft=(141, 71))
black_knight2_rect = black_knight2.get_rect(topleft=(491, 71))
black_pawn1_rect   = black_pawn1.get_rect(topleft=(71, 141))
black_pawn2_rect   = black_pawn2.get_rect(topleft=(141, 141))
black_pawn3_rect   = black_pawn3.get_rect(topleft=(211, 141))
black_pawn4_rect   = black_pawn4.get_rect(topleft=(281, 141))
black_pawn5_rect   = black_pawn5.get_rect(topleft=(351, 141))
black_pawn6_rect   = black_pawn6.get_rect(topleft=(421, 141))
black_pawn7_rect   = black_pawn7.get_rect(topleft=(491, 141))
black_pawn8_rect   = black_pawn8.get_rect(topleft=(561, 141))

white_rects = [
    white_king_rect, white_queen_rect,
    white_rook1_rect, white_rook2_rect,
    white_bishop1_rect, white_bishop2_rect,
    white_knight1_rect, white_knight2_rect,
    white_pawn1_rect, white_pawn2_rect, white_pawn3_rect, white_pawn4_rect,
    white_pawn5_rect, white_pawn6_rect, white_pawn7_rect, white_pawn8_rect,
]

black_rects = [
    black_king_rect, black_queen_rect,
    black_rook1_rect, black_rook2_rect,
    black_bishop1_rect, black_bishop2_rect,
    black_knight1_rect, black_knight2_rect,
    black_pawn1_rect, black_pawn2_rect, black_pawn3_rect, black_pawn4_rect,
    black_pawn5_rect, black_pawn6_rect, black_pawn7_rect, black_pawn8_rect,
]

# (surface, rect) tuples — solves the duplicate-key dict bug completely
white_pieces = [
    (white_king,    white_king_rect),
    (white_queen,   white_queen_rect),
    (white_rook1,   white_rook1_rect),
    (white_rook2,   white_rook2_rect),
    (white_bishop1, white_bishop1_rect),
    (white_bishop2, white_bishop2_rect),
    (white_knight1, white_knight1_rect),
    (white_knight2, white_knight2_rect),
    (white_pawn1,   white_pawn1_rect),
    (white_pawn2,   white_pawn2_rect),
    (white_pawn3,   white_pawn3_rect),
    (white_pawn4,   white_pawn4_rect),
    (white_pawn5,   white_pawn5_rect),
    (white_pawn6,   white_pawn6_rect),
    (white_pawn7,   white_pawn7_rect),
    (white_pawn8,   white_pawn8_rect),
]

black_pieces = [
    (black_king,    black_king_rect),
    (black_queen,   black_queen_rect),
    (black_rook1,   black_rook1_rect),
    (black_rook2,   black_rook2_rect),
    (black_bishop1, black_bishop1_rect),
    (black_bishop2, black_bishop2_rect),
    (black_knight1, black_knight1_rect),
    (black_knight2, black_knight2_rect),
    (black_pawn1,   black_pawn1_rect),
    (black_pawn2,   black_pawn2_rect),
    (black_pawn3,   black_pawn3_rect),
    (black_pawn4,   black_pawn4_rect),
    (black_pawn5,   black_pawn5_rect),
    (black_pawn6,   black_pawn6_rect),
    (black_pawn7,   black_pawn7_rect),
    (black_pawn8,   black_pawn8_rect),
]

something = None
registered_square_1 = None
registered_square_2 = None
stockfish_turn = (side == 'b')
player_move = None

castle_white_short = True
castle_white_long  = True
castle_black_short = True
castle_black_long  = True

def flip_mouse(mx, my):
    return 700 - mx, 700 - my

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            engine.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not stockfish_turn:
            mx, my = event.pos
            if side == 'b':
                mx, my = flip_mouse(mx, my)

            for name, square in squares.items():
                if square.collidepoint(mx, my):
                    if something is None:
                        something = name
                        registered_square_1 = square
                    else:
                        player_move = something + name

                        if chess.Move.from_uci(player_move) in board.legal_moves:
                            board.push(chess.Move.from_uci(player_move))
                            registered_square_2 = square

                            if side == 'w':
                                for index1, (piece, rect) in enumerate(white_pieces):
                                    if rect == registered_square_1:
                                        rect.x = registered_square_2.x
                                        rect.y = registered_square_2.y
                                        stockfish_turn = True

                                        if castle_white_long and white_king_rect == c1:
                                            white_rook1_rect.x = d1.x
                                            white_rook1_rect.y = d1.y
                                            castle_white_long = False
                                        if castle_white_short and white_king_rect == g1:
                                            white_rook2_rect.x = f1.x
                                            white_rook2_rect.y = f1.y
                                            castle_white_short = False
                                        if rect == white_rook1_rect: castle_white_long = False
                                        if rect == white_rook2_rect: castle_white_short = False
                                        if rect == white_king_rect:
                                            castle_white_long = False
                                            castle_white_short = False


                                        for index2, (bp, brect) in enumerate(black_pieces):
                                            if rect == brect:
                                                del black_pieces[index2]
                                                del black_rects[index2]
                                                break
                                        break

                            else:
                                for index1, (piece, rect) in enumerate(black_pieces):
                                    if rect == registered_square_1:
                                        rect.x = registered_square_2.x
                                        rect.y = registered_square_2.y
                                        stockfish_turn = True

                                        if castle_black_long and black_king_rect == c8:
                                            black_rook1_rect.x = d8.x
                                            black_rook1_rect.y = d8.y
                                            castle_black_long = False
                                        if castle_black_short and black_king_rect == g8:
                                            black_rook2_rect.x = f8.x
                                            black_rook2_rect.y = f8.y
                                            castle_black_short = False
                                        if rect == black_rook1_rect: castle_black_long = False
                                        if rect == black_rook2_rect: castle_black_short = False
                                        if rect == black_king_rect:
                                            castle_black_long = False
                                            castle_black_short = False

                                        for index2, (wp, wrect) in enumerate(white_pieces):
                                            if rect == wrect:
                                                del white_pieces[index2]
                                                del white_rects[index2]
                                                break
                                        break

                        else:
                            print("Illegal move:", player_move)
                            something = None
                            registered_square_1 = None
                            continue

                        something = None
                        registered_square_1 = None
                        registered_square_2 = None
                    break

    # Draw
    canvas.blit(Chessboard, (0, 0))
    for piece, rect in white_pieces:
        canvas.blit(piece, rect)
    for piece, rect in black_pieces:
        canvas.blit(piece, rect)

    # Stockfish turn
    if stockfish_turn:
        stockfish_move = engine.play(board, chess.engine.Limit(time=0.5))
        board.push(stockfish_move.move)
        STOCKFISH = str(stockfish_move.move)
        sf_from = squares[STOCKFISH[:2]]
        sf_to   = squares[STOCKFISH[2:]]

        if side == 'w':
            # Stockfish plays black
            for index3, (piece, rect) in enumerate(black_pieces):
                if rect == sf_from:
                    rect.x = sf_to.x
                    rect.y = sf_to.y

                    if castle_black_long and black_king_rect == c8:
                        black_rook1_rect.x = d8.x
                        black_rook1_rect.y = d8.y
                        castle_black_long = False
                    if castle_black_short and black_king_rect == g8:
                        black_rook2_rect.x = f8.x
                        black_rook2_rect.y = f8.y
                        castle_black_short = False
                    if rect == black_rook1_rect: castle_black_long = False
                    if rect == black_rook2_rect: castle_black_short = False
                    if rect == black_king_rect:
                        castle_black_long = False
                        castle_black_short = False

                    for index4, (wp, wrect) in enumerate(white_pieces):
                        if rect == wrect:
                            del white_pieces[index4]
                            del white_rects[index4]
                            break
                    break

        else:
            # Stockfish plays white
            for index3, (piece, rect) in enumerate(white_pieces):
                if rect == sf_from:
                    rect.x = sf_to.x
                    rect.y = sf_to.y

                    if castle_white_long and white_king_rect == c1:
                        white_rook1_rect.x = d1.x
                        white_rook1_rect.y = d1.y
                        castle_white_long = False
                    if castle_white_short and white_king_rect == g1:
                        white_rook2_rect.x = f1.x
                        white_rook2_rect.y = f1.y
                        castle_white_short = False
                    if rect == white_rook1_rect: castle_white_long = False
                    if rect == white_rook2_rect: castle_white_short = False
                    if rect == white_king_rect:
                        castle_white_long = False
                        castle_white_short = False

                    for index4, (bp, brect) in enumerate(black_pieces):
                        if rect == brect:
                            del black_pieces[index4]
                            del black_rects[index4]
                            break
                    break

        stockfish_turn = False

    if side == 'b':
        window.blit(pygame.transform.rotate(canvas, 180), (0, 0))
    else:
        window.blit(canvas, (0, 0))

    pygame.display.update()