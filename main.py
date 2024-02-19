"""
This file contains the main application logic for the game.
"""

import os

import pygame


pygame.font.init()
pygame.mixer.init()

from src.consts import *

pygame.display.set_caption("First Game")

from src.functs import *
from src.events_loop import *


def main():
    """This is the main function of the game. It contains the game loop."""

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()  # Création de l'instance de l'horloge
    run = True

    while run:
        red_health, yellow_health = main_loop(
            yellow_bullets,
            red_bullets,
            yellow,
            red,
            red_health,
            yellow_health,
            clock,
        )


if __name__ == "__main__":
    main()
