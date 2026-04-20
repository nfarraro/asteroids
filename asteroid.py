import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle_one = random.uniform(20.0, 50.0)
        angle_two = angle_one * -1
        velocity_one = self.velocity.rotate(angle_one)
        velocity_two = self.velocity.rotate(angle_two)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = velocity_one * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = velocity_two * 1.2
