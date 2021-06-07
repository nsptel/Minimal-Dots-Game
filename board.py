import string


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_axis = (''.join([str(i) for i in range(10)]) + string.ascii_uppercase)[:self.x]
        self.y_axis = (''.join([str(i) for i in range(10)]) + string.ascii_uppercase)[:self.y]
        self.vals = [[' ' for _ in range(self.x)] for _ in range(self.y)]
        self.hor_bars = [['   ' for _ in range(self.x)] for _ in range(self.y)]
        self.ver_bars = [[' ' for _ in range(self.x)] for _ in range(self.y)]
        self.moves = []
        self.generate_board()

    def generate_board(self):
        print('   ', end='')
        [print(f'{self.x_axis[i]}   ', end='') for i in range(len(self.x_axis))]
        print()
        for i in range(len(self.y_axis)):
            print(f'{self.y_axis[i]}  ', end='')
            for j in range(len(self.x_axis)):
                print(f'+{self.hor_bars[i][j]}', end='')
            print('\n   ', end='')
            for j in range(len(self.x_axis)):
                print(f'{self.ver_bars[i][j]} {self.vals[i][j]} ', end='')
            print()

    def make_move(self, a, b, player):
        cur_move = {a, b}
        try:
            assert(((a[0] == b[0] and abs(a[1] - b[1]) == 1) or (a[1] == b[1] and abs(a[0] - b[0]) == 1))
                   and cur_move not in self.moves)
        except AssertionError:
            print("Please enter a valid move...")
            return
        if a[0] == b[0]:
            self.hor_bars[a[0]][min(a[1], b[1])] = '---'
        else:
            self.ver_bars[min(a[0], b[0])][b[1]] = '|'
        self.moves.append(cur_move)
        self.occupy_box(a, b, player)

    def occupy_box(self, m, n, player):
        if m[0] == n[0]:
            if {m, (m[0]-1, m[1])} in self.moves and \
                    {(m[0]-1, m[1]), (n[0]-1, n[1])} in self.moves and \
                    {n, (n[0]-1, n[1])} in self.moves:
                self.vals[m[0]-1][min(m[1], n[1])] = player.id
                player.score += 1
            if {m, (m[0]+1, m[1])} in self.moves and \
                    {(m[0]+1, m[1]), (n[0]+1, n[1])} in self.moves and \
                    {n, (n[0]+1, n[1])} in self.moves:
                self.vals[m[0]][min(m[1], n[1])] = player.id
                player.score += 1
        if m[1] == n[1]:
            if {m, (m[0], m[1]-1)} in self.moves and \
                    {(m[0], m[1]-1), (n[0], n[1]-1)} in self.moves and \
                    {n, (n[0], n[1]-1)} in self.moves:
                self.vals[min(m[0], n[0])][m[1]-1] = player.id
                player.score += 1
            if {m, (m[0], m[1]+1)} in self.moves and \
                    {(m[0], m[1]+1), (n[0], n[1]+1)} in self.moves and \
                    {n, (n[0], n[1]+1)} in self.moves:
                self.vals[min(m[0], n[0])][m[1]] = player.id
                player.score += 1
        self.generate_board()


if __name__ == "__main__":
    from player import Player
    p = Player('N')
    game = Board(10, 10)
    game.make_move((3, 3), (3, 4), p)
    game.make_move((3, 3), (4, 3), p)
    game.make_move((4, 4), (3, 4), p)
    game.make_move((4, 3), (5, 3), p)
    game.make_move((5, 3), (5, 4), p)
    game.make_move((4, 4), (5, 4), p)
    game.make_move((4, 3), (4, 4), p)
    print(p.id, p.score)
