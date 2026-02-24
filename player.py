import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

# THE PLAYER IS A TRIANGLE, BUT THE HITBOX IS AN INVISIBLE CIRCLE, HENCE "CIRCLESHAPE"
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self, dt):
        shot_obj = Shot(self.position, self.rotation, SHOT_RADIUS)
        shot_obj.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot_obj.velocity *= PLAYER_SHOOT_SPEED
    
    def update(self, dt):

        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        # ROTATION (LEFT / RIGHT)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # MOVEMENT (UP / DOWN)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # SHOOTING
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot(dt)
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS