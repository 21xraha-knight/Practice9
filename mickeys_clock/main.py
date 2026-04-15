import pygame
import sys
import datetime
from clock import blit_rotate_center 

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 800 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Mouse Clock")
    
    bg = pygame.image.load("images/mickey_bg.png").convert_alpha()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    right_hand = pygame.image.load("images/right_hand.png").convert_alpha() 
    right_hand = pygame.transform.scale(right_hand, (120, 350)) 
    left_hand = pygame.image.load("images/left_hand.png").convert_alpha() 
    left_hand = pygame.transform.scale(left_hand, (100, 250))

    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    center = (center_x, center_y)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute

        sec_angle = second * 6
        min_angle = minute * 6
 
        screen.blit(bg, (0, 0))

        blit_rotate_center(screen, left_hand, center, sec_angle)
        blit_rotate_center(screen, right_hand, center, min_angle)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()