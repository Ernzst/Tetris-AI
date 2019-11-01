from board import Direction, Rotation
from random import Random

class Player:
    def move(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def move(self, board):
        return self.random.choice([
            Direction.Left,
            Direction.Right,
            Direction.Down,
            Rotation.Anticlockwise,
            Rotation.Clockwise,
        ])


SelectedPlayer = RandomPlayer
#SelectedPlayer = None
