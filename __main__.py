import sys
from player import Player
from board import Board


def print_score(players, over=False):
    if not over:
        print('Current Score >> ', end='')
        [print(f'{p.id}: {p.score}, ', end='') for p in players]
        print()
    else:
        highest_score = max([p.score for p in players])
        if highest_score == 0:
            print('No one scored enough to win the game!')
        else:
            winners = list(filter(lambda p: p.score == highest_score, players))
            if len(winners) > 1:
                print('This game was a tie between ' + ', '.join([w.id for w in winners]) +
                      f' with the score of {highest_score}')
            else:
                print(f'{winners[0].id} won the game with the score of {highest_score}')
        sys.exit(0)


def initialize():
    ids = []
    move_count = 1

    print('Welcome to the Minimal Dots Game!')
    while True:
        try:
            x, y = tuple(map(int, input('Enter board size (both axis should be greater than 1): ').split()))
            assert(x > 1 and y > 1)
            break
        except:
            print('Enter valid size in the form of "`x-axis size` `y-axis size`".')
            continue

    while True:
        n = input("Enter the number of players (between 2 and 5): ")
        if n.isnumeric() and 1 < int(n) < 6:
            n = int(n)
            break
        else:
            print("Please enter a valid input...")

    for i in range(n):
        while True:
            id = input(f'Enter one-character id for player {i+1}: ')
            if len(id) == 1 and id.isalpha() and id.upper() not in ids:
                break
            else:
                print('Please enter a valid id...')
        ids.append(id.upper())
    board = Board(x, y)
    players = [Player(id) for id in ids]

    while move_count <= 2 * x * y - (x + y):
        cur_player = players[(move_count - 1) % len(players)]
        inp = input(f'Player {cur_player.id}\'s move (press `0` to announce the score and leave the game): ')
        try:
            if inp.strip() == '0':
                print_score(players, over=True)
                break
            a, b = inp.split(',')
            a = tuple(map(int, a.split()))
            b = tuple(map(int, b.split()))
            assert((a[0] == b[0] and abs(a[1] - b[1]) == 1) or
                   (a[1] == b[1] and abs(a[0] - b[0]) == 1) and
                   {a, b} not in board.moves)
        except AssertionError as e:
            print('Move should be exactly 1 step and different from any earlier moves, please try again.')
            continue
        except Exception as e:
            print('Please enter a valid move...')
            continue
        board.make_move(a, b, cur_player)
        print_score(players)
        move_count += 1
    print_score(players, over=True)


if __name__ == "__main__":
    initialize()
