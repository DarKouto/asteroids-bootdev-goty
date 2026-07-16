import pygame, sys
from logger import log_state, log_event
from constants import *
from customfunctions import *
from player import Player
from asteroidfield import AsteroidField

def main():
    welcome_screen() # PRINT INFO AND INSTRUCTIONS
    pygame.init() # INITIALIZE PYGAME
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # DRAW SCREEN
    clock = pygame.time.Clock() # SET FPS
    dt = 0 # SET DELTA TIME 
    updatable, drawable, asteroids, shots = create_groups() # ADD OBJECTS TO GROUPS
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # SPAWN PLAYER IN THE MIDDLE OF THE SCREEN
    AsteroidField() # CREATE ASTEROID FIELD
    score = 0

    # GAME LOOP
    while True:
        log_state() # for boot.dev logging purposes

        # CLOSE WINDOW
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
         # PLAYER MOVEMENT
        updatable.update(dt)

        # COLLISIONS: ASTEROID VS PLAYER
        for asteroid in asteroids:
            if asteroid.collides_with(player_obj):
                log_event("player_hit")
                print("Game over!")
                print(f"Final Score: {score}")
                sys.exit(0)
        
        # COLLISIONS: ASTEROID VS SHOT
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score+=1

        # CLEAN SCREEN / DRAW PLAYER
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        # REFRESH THE SCREEN / SET FRAME RATE
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()