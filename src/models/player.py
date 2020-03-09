import abc


class Player(abc.ABC):
    """
    Class to represent a player
    """

    def __init__(self, fences: list):
        self.fences = fences


    @abc.abstractmethod
    def make_move(self) -> None:
        """
        Abstract method for make move

        Returns:
            None
        """
        pass



