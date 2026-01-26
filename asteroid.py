import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            vector_new1 = self.velocity.rotate(split_angle)
            vector_new2 = self.velocity.rotate(-split_angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            split_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius)
            split_asteroid1.velocity = vector_new1 * 1.2
            split_asteroid2.velocity = vector_new2 * 1.2