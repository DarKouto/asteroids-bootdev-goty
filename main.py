import pygame, sys
from logger import log_state, log_event
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids with pygame version: 2.6.1!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # INITIALIZE PYGAME / DRAW SCREEN
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS / DELTA TIME
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS / EVERYTIME AN OBJECT IS CREATED, IT'S ADDED TO A GROUP
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

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
        
        # COLLISIONS: SHOT VS ASTEROID
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()

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
