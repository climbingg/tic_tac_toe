"""把table.txt做出來"""


table = set()


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


def dfs(board: list[list[int]], board_is_empty: list[list[bool]], bout: int) -> int:
    """優先深度搜索，找出所有可能的是否獲勝"""
    if bout == 10:
        return 0
    if bout % 2 == 1:
        chess = 1
    else:
        chess = -1
    end_score_li = []
    for y in range(3):
        for x in range(3):
            if not board_is_empty[y][x]:
                end_score_li.append(None)
                continue
            board[y][x] = chess
            board_is_empty[y][x] = False
            if check_whether_win(board, chess):
                end_score_li.append(chess)
            else:
                end_score_li.append(dfs(board, board_is_empty, bout + 1))
            board[y][x] = 0
            board_is_empty[y][x] = True
    one_of_table = []
    for y in range(3):
        for x in range(3):
            one_of_table.append(str(board[y][x]))
    table.add(f"{" ".join(one_of_table)}  {" ".join(list(map(str, end_score_li)))}")
    if chess == 1:
        return max(end_score_li, key=lambda x: -2 if x is None else x)
    return min(end_score_li, key=lambda x: 2 if x is None else x)


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board_is_empty = [[True, True, True], [True, True, True], [True, True, True]]

dfs(board, board_is_empty, 1)

with open("table.txt", "w", encoding="ascii") as file:
    for i, one_board in enumerate(table):
        if i == len(table) - 1:
            file.write(one_board)
        else:
            file.write(f"{one_board}\n")
