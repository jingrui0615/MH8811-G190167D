import random


def TicTacShape(n):
    if int(n) == 0:
        item = "O"
    elif int(n) == 1:
        item = "X"
    elif int(n) == 2:
        item = " "
    else:
        print("[Error]: unexpected value in list")
        exit(1)
    return item


def TicTacDraw(board):
    board_draw = []
    gap = ''
    for i in range(2 * len(board)):
        gap += '-'
    for rows in board:
        rows_draw = []
        for item in rows:
            rows_draw.append(TicTacShape(item))
        rows_draw_str = '|'.join(rows_draw)
        board_draw.append(rows_draw_str)
    board_draw_str = ("\n" + gap + "\n").join(board_draw)
    print(board_draw_str)


if __name__ == '__main__':
    dim = random.randint(1, 100)
    board = [[random.randint(0, 2) for _ in range(dim)] for _ in range(dim)]
    print(board)
    TicTacDraw(board)
