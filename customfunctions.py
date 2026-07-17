import pygame
from constants import *
from asteroid import Asteroid
from shot import Shot
from player import Player
from asteroidfield import AsteroidField

def welcome_screen():
    print("\n====================\n")
    print("Starting Asteroids with pygame version: 2.6.1!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("\n====================\n")
    print("HOW TO PLAY:")
    print(" - Use the WASD keys to move the spaceship")
    print(" - Use the SPACE key to shoot")
    print(" - Everytime the spaceship collides with an asteroid you lose a life")
    print(" - The game ends when you run out of lives")

    print("\n====================\n")
    input("Press ENTER to start the game")

def create_groups():
    # GROUPS / EVERYTIME AN OBJECT IS CREATED, IT'S ADDED TO A GROUP
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    return updatable, drawable, asteroids, shots

def check_score(score):
    score_board = pygame.font.Font(None, 36)
    return score_board.render(f"Score: {score}", True, "white")

def check_lives(lives):
    lives_board = pygame.font.Font(None, 36)
    if lives == 3:
        return lives_board.render(f"Lives: {lives}", True, "white")
    elif lives == 2:
        return lives_board.render(f"Lives: {lives}", True, "yellow")
    elif lives == 1:
        return lives_board.render(f"Lives: {lives}", True, "red")