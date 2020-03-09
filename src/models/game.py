from src.models.board import Board
from src.models.player import Player


class Game(object):
    def __init__(self, player_1: Player, player_2: Player, board: Board) -> None:
        """
        Initialises the game
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
