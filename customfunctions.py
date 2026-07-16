import pygame
from constants import *
from asteroid import Asteroid
from shot import Shot
from player import Player
from asteroidfield import AsteroidField

def welcome_screen():
    print("")
    print("====================\n")

    print("Starting Asteroids with pygame version: 2.6.1!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    print("")
    print("====================\n")

    print("HOW TO PLAY:")
    print(" - Use the WASD keys to move the spaceship")
    print(" - Use the SPACE key to shoot")
    print(" - The game ends when the spaceship collides with an asteroid")

    print("")
    print("====================\n")

    input("Press ENTER to start the game")

def create_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    return updatable, drawable, asteroids, shots