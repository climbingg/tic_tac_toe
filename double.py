import random


class board:
    def __init__(self) -> None:
        self.centent = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.BLUE = "\033[94m"
        self.RESET = "\033[0m"

    def print_board(self):
        my_table = [
            self.BLUE + "+" + self.RESET,
            self.RED + "o" + self.RESET,
            self.GREEN + "x" + self.RESET,
        ]
        for i in self.centent:
            for j in i:
                print(end=my_table[j])
            print()

    def check_straight_up_dwon(self, check_num: int) -> bool:
        for x in range(3):
            count = 0
            for y in range(3):
                if self.centent[y][x] == check_num:
                    count += 1
            if count == 3:
                return True
        return False

    def check_straight_left_right(self, check_num: int) -> bool:
        for y in range(3):
            count = 0
            for x in range(3):
                if self.centent[y][x] == check_num:
                    count += 1
            if count == 3:
                return True
        return False

    def check_diagonal_left_up_to_rigth_down(self, check_num: int) -> bool:
        for x_y in range(3):
            if self.centent[x_y][x_y] != check_num:
                return False
        return True

    def check_diagonal_right_up_to_left_down(self, check_num: int) -> bool:
        for x_y in range(3):
            if self.centent[x_y][2 - x_y] != check_num:
                return False
        return True

    def check_win(self, check_num: int) -> bool:
        check_func = [
            self.check_straight_up_dwon,
            self.check_straight_left_right,
            self.check_diagonal_left_up_to_rigth_down,
            self.check_diagonal_right_up_to_left_down,
        ]
        for i in check_func:
            if i(check_num):
                return True
        return False

    def circle_play(self, x: int, y: int) -> bool:
        self.centent[3 - y][x - 1] = 1
        return self.check_win(1)

    def chacha_play(self, x: int, y: int) -> bool:
        self.centent[3 - y][x - 1] = 2
        return self.check_win(2)


now_board = board()

legal = {"1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"}

while True:
    now_board.print_board()
    if len(legal) == 0:
        print("平局!!")
        break
    user_input = input("輸入一個座標:")
    while user_input not in legal:
        user_input = input(f"你剛才輸入的不是合法棋步，輸入一個座標，例如{random.choice(list(legal))}:")
    legal.remove(user_input)
    if len(legal) % 2 == 0:
        if now_board.circle_play(int(user_input[0]), int(user_input[2])):
            now_board.print_board()
            print("圈圈獲勝!!")
            break
    else:
        if now_board.chacha_play(int(user_input[0]), int(user_input[2])):
            now_board.print_board()
            print("叉叉獲勝!!")
            break

print("遊戲結束!!")
