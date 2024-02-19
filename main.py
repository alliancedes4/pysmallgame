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


def loop_event(
    yellow_bullets,
    red_bullets,
    yellow,
    red,
    red_health,
    yellow_health,
):
    """main manager for event loop in the game."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(
                    yellow.x + yellow.width,
                    yellow.y + yellow.height // 2 - 2,
                    10,
                    5,
                )
                yellow_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()

            if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                red_bullets.append(bullet)
                BULLET_FIRE_SOUND.play()

        if event.type == RED_HIT:
            red_health -= 1
            BULLET_HIT_SOUND.play()

        if event.type == YELLOW_HIT:
            yellow_health -= 1
            BULLET_HIT_SOUND.play()

    return red_health, yellow_health


def main_loop(
    yellow_bullets, red_bullets, yellow, red, red_health, yellow_health, clock
):
    clock.tick(FPS)

    red_health, yellow_health = loop_event(
        yellow_bullets,
        red_bullets,
        yellow,
        red,
        red_health,
        yellow_health,
    )

    winner_text = ""
    if red_health <= 0:
        winner_text = "Yellow Wins!"

    if yellow_health <= 0:
        winner_text = "Red Wins!"

    if winner_text != "":
        draw_winner(winner_text)
        # break

        # NOTE Maybe problematic due to expected break loop

        return 0

    keys_pressed = pygame.key.get_pressed()

    yellow_handle_movement(keys_pressed, yellow)
    red_handle_movement(keys_pressed, red)

    handle_bullets(yellow_bullets, red_bullets, yellow, red)

    draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    return red_health, yellow_health


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
