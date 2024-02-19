"""
This file contains all the constants used in the game.
"""

import os

import pygame

# os.path.join(os.path.dirname(__file__), "assets")
ASSETS_DIR = "./assets/"
IMG_DIR = os.path.join(ASSETS_DIR, "imgs")
SOUND_DIR = os.path.join(ASSETS_DIR, "sounds")


grenade = os.path.join(SOUND_DIR, "Grenade+1.mp3")
gun = os.path.join(SOUND_DIR, "Gun+Silencer.mp3")
spaceship_red = os.path.join(IMG_DIR, "spaceship_red.png")
spaceship_yellow = os.path.join(IMG_DIR, "spaceship_yellow.png")
space = os.path.join(IMG_DIR, "space.png")

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)


# TODO: Debug this
BULLET_HIT_SOUND = pygame.mixer.Sound(grenade)
BULLET_FIRE_SOUND = pygame.mixer.Sound(gun)


HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(spaceship_yellow))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)

RED_SPACESHIP_IMAGE = pygame.image.load(spaceship_red)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)

SPACE = pygame.transform.scale(pygame.image.load(space), (WIDTH, HEIGHT))
