import pygame

def blit_rotate_center(surface, image, center, angle):

    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=center)
    surface.blit(rotated_image, new_rect)