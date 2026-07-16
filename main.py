import pygame, sys
from logger import log_state, log_event
from constants import *
from customfunctions import *
from player import Player
from asteroidfield import AsteroidField

def main():
    welcome_screen()

    # INITIALIZE PYGAME
    pygame.init()
    
    # DRAW SCREEN
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # SET FPS / DELTA TIME
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS / EVERYTIME AN OBJECT IS CREATED, IT'S ADDED TO A GROUP
    updatable, drawable, asteroids, shots = create_groups()

    # CREATE PLAYER / ASTEROID OBJECT
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # GAME LOOP
    while True:
        log_state() #for boot.dev logging purposes

        # CLOSING WINDOW
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # PLAYER MOVEMENT
        updatable.update(dt)

        # COLLISIONS: PLAYER VS ASTEROID
        for asteroid in asteroids:
            if asteroid.collides_with(player_obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)
        
        # ASTEROID IS SHOT
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # CLEAN SCREEN / DRAW PLAYER
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        # REFRESH THE SCREEN / SET FRAME RATE
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()