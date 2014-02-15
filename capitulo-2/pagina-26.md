26 http://inventwithpython.com/pygame

    1.  import pygame, sys
    2.  from pygame.locals import *
    3. 
    4.  pygame.init()
    5. 
    6.  FPS = 30 # frames per second setting
    7.  fpsClock = pygame.time.Clock()  
    8. 
    9.  #set up the window
    10. DISPLAYSURF = pygame.display.set_mode((400, 300),0 ,32)
    11. pygame.display.set_caption("Animation")
    12. 
    13. WHITE = (255, 255, 255)
    14. catImg = pygame.image.load('cat.png')
    15. catx = 10
    16. caty = 10
    17. direction = 'right'
    18. 
    19. while True: # the main game loop
    20.     DISPLAYSURF.fill(WHITE)
    21.     
    22.     if direction == 'right':
    23.         catx +=5
    24.         if catx == 280:
    25.             direction = 'down'
    26.     elif direction == 'down':
    27.         caty +=5
    28.         if caty == 220:
    29.             direction = 'left'
    30.     elif direction == 'left':
    31.         catx -= 5
    32.         if catx == 10:
    33.             direction = 'up'
    34.     elif direction == 'up':
    35.         caty -= 5
    36.         if caty == 10:
    37.             direction = 'right'
    38. 
    39.     DISPLAYSURF.blit(catImg, (catx, caty))
    40. 
    41.     for event in pygame.event.get():
    42.         if event.type == QUIT:
    43.             pygame.quit()
    44.             sys.exit()
    45. 
    46.     pygame.display.update()
    

> Mande dúvidas por E-mail para o autor: al@inventwithpython.com