import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
done = False
is_blue = True
if is_blue: color = (0, 128, 255)
else: color = (255, 100, 0)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()