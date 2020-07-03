from src.constants import BOARD_HEIGHT, BOARD_WIDTH
from src.models.board import Board
from src.models.cell import Cell
from src.models.game import Game
from src.models.player_factory import PlayerFactory
from src.models.player_info import PlayerInfo


class Play:
    @staticmethod
    def get_board() -> Board:
        cells = []
        for row in range(BOARD_WIDTH):
            for column in range(BOARD_HEIGHT):
                cells.append(Cell(row + 1, column + 1))
        return Board(cells)

    @staticmethod
    def get_player(player_number: int, info: PlayerInfo, is_bot: bool = False):
        return PlayerFactory.get_class(is_bot)(player_number, info)


if __name__ == "__main__":
    board = Play.get_board()
    player_1 = Play.get_player(1, PlayerInfo("player_1", 1))
    player_2 = Play.get_player(2, PlayerInfo("player_2", 1))
    game = Game(player_1, player_2, board)
