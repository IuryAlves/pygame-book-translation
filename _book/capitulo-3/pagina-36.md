36 http://inventwithpython.com/pygame

    39. SQUARE = 'square'
    40. DIAMOND = 'diamond'
    41. LINES = 'lines'
    42. OVAL = 'oval'
    43. 
    44. ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
    45. ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
    46. assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,
    "Board is too big for the number of shapes/colors defined."
    47.
    48. def main():
    49.     global FPSCLOCK, DISPLAYSURF
    50.     pygame.init()
    51.     FPSCLOCK = pygame.time.Clock()
    52.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    53. 
    54.     mousex = 0 # used to store x coordinate of mouse event
    55.     mousey = 0 # used to store y coordinate of mouse event
    56.     pygame.display.set_caption('Memory Game')
    57. 
    58.     mainBoard = getRandomizedBoard()
    59.     revealedBoxes = generateRevealedBoxesData(False)
    60.      
    61.     firstSelection = None # stores the (x, y) of the first box clicked. 
    62. 
    63.     DISPLAYSURF.fill(BGCOLOR)
    64.     startGameAnimation(mainBoard)
    65. 
    66.     while True: # main game loop
    67.     mouseClicked = False
    68. 
    69.     DISPLAYSURF.fill(BGCOLOR) # drawing the window
    70.     drawBoard(mainBoard, revealedBoxes)
    71.     
    72.     for event in pygame.event.get(): # event handling loop
    73.         if event.type == QUIT or (event.type == KEYUP and event.key ==
    K_ESCAPE):
    74.             pygame.quit()
    75.             sys.exit()
    76.         elif event.type == MOUSEMOTION:
    77.             mousex, mousey = event.pos
    78.         elif event.type == MOUSEBUTTONUP:
    79.             mousex, mousey = event.pos
    80.             mouseClicked = True
    81.
    82.     boxx, boxy = getBoxAtPixel(mousex, mousey)

> Mande dúvidas por E-mail para: al@inventwithpython.com

