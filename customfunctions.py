from constants import *

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
    pass