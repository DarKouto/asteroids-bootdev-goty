import pygame
from logger import log_state
from constants import *
from player import Player

def main():
    # TERMINAL MESSAGES TO CHECK IF EVERYTHING IS OK
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

    # PLAYER
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_obj = Player(x,y)
    
    # GAME LOOP
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # PLAYER MOVEMENT
        player_obj.update(dt)
        # Clean Screen
        screen.fill("black")
        # Draw Player
        player_obj.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # Control frame rate
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()