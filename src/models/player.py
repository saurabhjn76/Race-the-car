import abc

from src.constants import BOARD_WIDTH, BOARD_HEIGHT
from src.models.fence import Fence
from src.models.player_info import PlayerInfo
from src.models.position import Position


class Player(abc.ABC):
    """
    Class to represent a player
    """
    def __init__(self, player_number: int, player_info: PlayerInfo, fence_count: int = 8):
        self.fences = [ Fence() for _ in range(fence_count)]
        self.player_info = player_info

        self.current_position =  Position(1, BOARD_WIDTH//2) if player_number==1 \
            else Position(BOARD_HEIGHT, BOARD_WIDTH//2)
        self.destination = Position(BOARD_HEIGHT, BOARD_WIDTH//2) if player_number==1 \
            else Position(1, BOARD_WIDTH//2)


    def get_remaining_fence_count(self):
        return len(self.fences)

    @abc.abstractmethod
    def make_move(self) -> None:
        """
        Abstract method for make move

        Returns:
            None
        """
        pass
