from src.players.computer_player import ComputerPlayer
from src.players.human_player import HumanPlayer


class PlayerFactory:
    @staticmethod
    def get_class(is_bot: bool):
        if is_bot:
            return ComputerPlayer
        return HumanPlayer