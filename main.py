import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.display.set_caption("Asterooooids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    obj.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
