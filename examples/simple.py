import pygame
from pygame.ext.spritesheets import SpriteSheet
import sys

    


def main():
    pygame.init()
    screen = pygame.display.set_mode((510, 255))
    clock = pygame.time.Clock()
    
    blocks = SpriteSheet("assets/blocks.png")

    dirt = pygame.transform.scale(blocks.image_at(pygame.Rect((192,  64),  (192,  128)),  (64,  64)),  (255,  255)) 
    water = pygame.transform.scale(blocks.image_at(pygame.Rect((64,  0),  (128,  64)),  (64, 64)),  (255,  255)) 
    
    
    
    while 1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        
        screen.blit(dirt,  (0, 0))
        screen.blit(water,  (256, 0))
        pygame.display.flip()
        clock.tick(-1)
        

if __name__ == "__main__":
    main()
    
    
    
    
