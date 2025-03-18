import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock= pygame.time.Clock()
    dt = 0

    posx = SCREEN_WIDTH / 2
    posy = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, rocks)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullets)

    player = Player(posx, posy)
    field = AsteroidField()

    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill((0, 0, 0))  # Black background
        
        updatable.update(dt)
        for rock in rocks:
            if rock.collision(player):
                print("GAME OVER!")
                exit()
            for bullet in bullets:
                if rock.collision(bullet):
                    rock.split()
                    bullet.kill()
        for item in drawable:
            item.draw(screen)

        # Update the display
        pygame.display.flip()

        dt = clock.tick(60) / 1000

   
    

if __name__ == "__main__":
    main()
