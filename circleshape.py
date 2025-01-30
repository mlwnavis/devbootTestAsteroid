import pygame

class CircleShape(pygame.sprite.Sprite):

    containers = ()
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0),
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def collisions(self, circle):
        distance = self.position.distance_to(circle.position)
        if distance <= self.radius + circle.radius:
            return True
        else:
            return False
