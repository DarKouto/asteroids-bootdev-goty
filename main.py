import pygame, sys
from logger import log_state, log_event
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    print("Starting Asteroids with pygame version: 2.6.1!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # INITIALIZE PYGAME
    pygame.init()

    # DRAW SCREEN
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS / DELTA TIME
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS / EVERYTIME AN OBJECT IS CREATED, IT IS ADDED TO A GROUP
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # CREATE PLAYER / ASTEROID OBJECT
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_obj = AsteroidField()

    # GAME LOOP
    while True:
        log_state() #for boot.dev logging purposes
        for event in pygame.event.get(): # for the window close
            if event.type == pygame.QUIT:
                return
        
        # PLAYER MOVEMENT
        updatable.update(dt)

        # CHECK COLLISIONS
        for asteroid in asteroids:
            if asteroid.collides_with(player_obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)

        # Clean Screen
        screen.fill("black")
        # Draw Player
        for item in drawable:
            item.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # Control frame rate
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()