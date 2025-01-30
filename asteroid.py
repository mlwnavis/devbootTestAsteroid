import pygame.draw
import random
import circleshape
from constants import *

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ang = random.uniform(20, 50)
            vec1, vec2 = self.velocity.rotate(ang) * 1.2, self.velocity.rotate(-ang) * 1.2
            radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1, Asteroid2 = Asteroid(self.position[0], self.position[1], radius), Asteroid(self.position[0], self.position[1], radius)
            Asteroid1.velocity, Asteroid2.velocity = vec1, vec2