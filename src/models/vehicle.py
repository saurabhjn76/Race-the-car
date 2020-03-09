import pygame

from src.models.color import Color


class Vehicle:
    """
    A class for vehicle
    """
    pass


class Car(Vehicle):
    """
    Car's class
    """

    def __init__(self, color: Color, img_path: str):
        self.color = color
        # TODO: add better code
        self.image = pygame.image.load(img_path)
