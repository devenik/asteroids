import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    #Game configs
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    #Group creation
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()
    #Group assignment
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    #Player and field spawning
    ast_field: AsteroidField = AsteroidField()
    player: Player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    #Game launch and loop
    while True:
        #Log creation
        log_state()
        #Quitting when hitting the X button on the top
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Background color setting
        screen.fill("black")
        #object refreshing
        updatable.update(dt)
        #Group behavior
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for d in drawable:
            d.draw(screen)
        #Screen refreshing and redrawing
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
