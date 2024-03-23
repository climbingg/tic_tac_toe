"""
ai分析器
黃色是已下過
綠色是會獲勝
藍色是會平手
紅色是會輸
"""

import random


def check_whether_win(board: list[list[int]], chess: int) -> bool:
    """檢查使否chess方連成一條線"""
    for y in range(3):
        if set(board[y]) == {chess}:
            return True
    for x in range(3):
        if {board[0][x], board[1][x], board[2][x]} == {chess}:
            return True
    if {board[0][0], board[1][1], board[2][2]} == {chess}:
        return True
    if {board[0][2], board[1][1], board[2][0]} == {chess}:
        return True
    return False


with open("table.txt", encoding="ascii") as file:
    table = file.read().split("\n")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

my_table = {
    -1: GREEN + "x" + RESET,
    0: BLUE + "+" + RESET,
    1: RED + "o" + RESET,
}

legal = {"1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"}

table_dict = {}
for one_of_table in table:
    key, value = one_of_table.split("  ")
    table_dict[key] = value


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board_is_empty = [[True, True, True], [True, True, True], [True, True, True]]

win_loss = 0

for bout in range(1, 10):
    if bout % 2 == 1:
        chess = 1
    else:
        chess = -1
    for i in board:
        for j in i:
            print(end=my_table[j])
        print()
    print()
    li = table_dict[" ".join([str(val) for row in board for val in row])]
    li = li.split()
    num_x_y_li = []
    for i, j in enumerate(li):
        if j == "None":
            print(end=YELLOW + "O" + RESET)
            if i % 3 == 2:
                print()
            continue
        num_x_y_li.append((int(j), (i % 3, i // 3)))
        print(end=[RED, BLUE, GREEN][::chess][int(j) + 1] + "O" + RESET)
        if i % 3 == 2:
            print()
    print()
    user_answer = input("輸入一個座標:")
    while user_answer not in legal:
        user_answer = input(f"你剛才輸入的不是合法棋步，輸入一個座標，例如{random.choice(list(legal))}:")
    legal.remove(user_answer)
    board[2 - int(user_answer.split(",")[1]) + 1][int(user_answer.split(",")[0]) - 1] = chess
    board_is_empty[2 - int(user_answer.split(",")[1]) + 1][int(user_answer.split(",")[0]) - 1] = False
    if check_whether_win(board, chess):
        if bout % 2 == 1:
            win_loss = 1
        else:
            win_loss = -1
        break

for i in board:
    for j in i:
        print(end=my_table[j])
    print()
print()

if win_loss == 1:
    print("圈圈贏了!!!!")

if win_loss == -1:
    print("叉叉贏了!!!!")

if win_loss == 0:
    print("平手!!!!")
