class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0


if __name__ == "__main__":
    from board import Board
    p = Player('N')
    board = Board(10, 10)
    board.make_move((0, 0), (0, 1), p)
