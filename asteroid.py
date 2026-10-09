import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        
        new1 = Asteroid(self.position.x, self.position.y, newRadius)
        new2 = Asteroid(self.position.x, self.position.y, newRadius)

        new1.velocity = v1 * 1.2
        new2.velocity = v2 * 1.2

        