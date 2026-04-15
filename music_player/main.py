import pygame
import sys
from player import MusicPlayer

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Keyboard Music Player")
    
    font = pygame.font.SysFont("Arial", 24)
    title_font = pygame.font.SysFont("Arial", 36, bold=True)

    player = MusicPlayer("music")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.prev_track()
                elif event.key == pygame.K_q: 
                    running = False

        screen.fill((30, 30, 40))

        title_text = title_font.render("Pygame Music Player", True, (255, 255, 255))
        track_text = font.render(f"Now Playing: {player.get_current_track_name()}", True, (100, 200, 255))
        status_text = font.render(f"Status: {'Playing' if player.is_playing else 'Stopped'}", True, (255, 255, 255))
        
        controls_text1 = font.render("Controls: P=Play, S=Stop", True, (150, 150, 150))
        controls_text2 = font.render("N=Next, B=Prev, Q=Quit", True, (150, 150, 150))

        screen.blit(title_text, (20, 20))
        screen.blit(track_text, (20, 100))
        screen.blit(status_text, (20, 150))
        screen.blit(controls_text1, (20, 250))
        screen.blit(controls_text2, (20, 290))

        pygame.display.flip()
        clock.tick(30) 

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()