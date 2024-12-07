import random

import pygame

from constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
            asteroids.add(asteroid1)
            asteroids.add(asteroid2)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt