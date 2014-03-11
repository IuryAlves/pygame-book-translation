40 http://inventwithpython.com/pygame

    204.    # color value for x, y spot is stored in board[x][y][1]
    205.    return board[boxx][boxy][0], board[boxx][boxy][1]
    206. 
    207.    
    208. def drawBoxCovers(board, boxes, coverage):
    209.    # Draws boxes being covered/revealed. "boxes" is a list
    210.    # of two-item lists, which have the x & y spot of the box.
    211.    for box in boxes:
    212.        left, top = leftTopCoordsOfBox(box[0], box[1])
    213.        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE,
BOXSIZE))
    214.        shape, color = getShapeAndColor(board, box[0], box[1])
    215.        drawIcon(shape, color, box[0], box[1])
    216.        if coverage > 0: # only draw the cover if there is an coverage
    217.            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    218.    pygame.display.update()
    219.    FPSCLOCK.tick(FPS)
    220. 
    221.
    222. def revealBoxesAnimation(board, boxesToReveal):
    223.    # Do the "box reveal" animation.
    224.    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, - REVEALSPEED):
    225.        drawBoxCovers(board, boxesToReveal, coverage)
    226. 
    227.
    228. def coverBoxesAnimation(board, boxesToCover):
    229.    # Do the "box cover" animation.
    230.    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
    231.        drawBoxCovers(board, boxesToCover, coverage)
    232. 
    233.
    234. def drawBoard(board, revealed):
    235.    # Draws all of the boxes in their covered or revealed state.
    236.    for boxx in range(BOARDWIDTH):
    237.        for boxy in range(BOARDHEIGHT):
    238.            left, top = leftTopCoordsOfBox(boxx, boxy)
    239.            if not revealed[boxx][boxy]:
    240.                # Draw a covered box.
    241.                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top,
BOXSIZE, BOXSIZE))
    242.            else:
    243.                # Draw the (revealed) icon.
    244.                shape, color = getShapeAndColor(board, boxx, boxy)
    245.                drawIcon(shape, color, boxx, boxy)
    246. 

   > Mande dúvidas por E-mail para: al@inventwithpython.com 

   
