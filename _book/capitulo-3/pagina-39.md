Capítulo 3 - Jogo da memória 39

    167.    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    168.    return (left, top)
    169. 
    170.
    171. def getBoxAtPixel(x, y):
    172.    for boxx in range(BOARDWIDTH):
    173.        for boxy in range(BOARDHEIGHT):
    174.            left, top = leftTopCoordsOfBox(boxx, boxy)
    175.            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
    176.            if boxRect.collidepoint(x, y):
    177.                return (boxx, boxy)
    178.    return (None, None)
    179. 
    180.
    181. def drawIcon(shape, color, boxx, boxy):
    182.    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    183.    half = int(BOXSIZE * 0.5) # syntactic sugar
    184. 
    185.    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from
board coords
    186.    # Draw the shapes
    187.    if shape == DONUT:
    188.        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
    189.        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top +
half), quarter - 5)
    190.    elif shape == SQUARE:
    191.        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top +
quarter, BOXSIZE - half, BOXSIZE - half))
    192.    elif shape == DIAMOND:
    193.        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    194.    elif shape == LINES:
    195.        for i in range(0, BOXSIZE, 4):
    196.            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
    197.            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    198.    elif shape == OVAL:
    199.        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter,
BOXSIZE, half))
    200.
    201.
    202. def getShapeAndColor(board, boxx, boxy):
    203.    # shape value for x, y spot is stored in board[x][y][0]
    204. 
