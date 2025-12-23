# LINUX RUNNING INSTRUCTIONS
# 
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -e .[dev]

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption(project_name)

# init text support
pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
   
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # write text
    text_surface = my_font.render('Hello, world!', False, (255, 0, 0))
    screen.blit(text_surface, (0, 0))

    # update/draw
    pygame.display.flip()
pygame.quit()
