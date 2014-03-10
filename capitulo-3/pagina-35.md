Capítulo 3 jogo da Memória 35

mensagem de erro e procure por erros no seu código.Você também pode copiar e colar seu código no site http://invpy.com/diff/memorypuzzle para verificar alguma diferença entre o seu código e o código do livro.

Você irá provavelmente ter algumas ideias de como jogos de computador funcionam.E quando você terminar de digitar, você pode ficar com o jogo para você.

    1.  # Memory puzzle
    2.  # By Al Sweigart al@inventwithpython.com
    3.  # http://inventwithpython.com/pygame
    4.  # Released under a "Simplified BSD" license
    5. 
    6.  import random, pygame, sys
    7.  from pygame.locals import *
    8. 
    9.  FPS = 30 # frames per second, the general speed of the program
    10. WINDOWWIDTH = 640 # size of window's width in pixels
    11. WINDOWHEIGHT = 480 # size of windows' height in pixels
    12. REVEALSPEED = 8 # speed boxes' sliding reveals and covers
    13. BOXSIZE = 40 # size of box height & width in pixels
    14. GAPSIZE = 10 # size of gap between boxes in pixels
    15. BOARDWIDTH = 10 # number of columns of icons
    16. BOARDHEIGHT = 7 # number of rows of icons
    17. assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
    18. XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
    19. YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
    20. 
    21. #   R   G   B
    22. GRAY = (100, 100, 100)
    23. NAVYBLUE = ( 60, 60, 100)
    24. WHITE = (255, 255, 255)
    25. RED = (255,0, 0)
    26. GREEN = ( 0, 255, 0)
    27. BLUE = ( 0, 0, 255)
    28. YELLOW = (255, 255, 0)
    29. ORANGE = (255, 128, 0)
    30. PURPLE = (255, 0, 255)
    31. CYAN = ( 0, 255, 255)
    32. 
    33. BGCOLOR = NAVYBLUE
    34. LIGHTBGCOLOR = GRAY
    35. BOXCOLOR = WHITE
    36. HIGHLIGHTCOLOR = BLUE
    37. 
    38. DONUT = 'donut'
