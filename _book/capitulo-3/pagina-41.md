Capítulo 3 - Jogo da memória 41

    247.
    248. def drawHighlightBox(boxx, boxy):
    249.    left, top = leftTopCoordsOfBox(boxx, boxy)
    250.    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5,
BOXSIZE + 10, BOXSIZE + 10), 4)
    251.
    252.
    253. def startGameAnimation(board):
    254.    # Randomly reveal the boxes 8 at a time.
    255.    coveredBoxes = generateRevealedBoxesData(False)
    256.    boxes = []
    257.    for x in range(BOARDWIDTH):
    258.        for y in range(BOARDHEIGHT):
    259.            boxes.append( (x, y) )
    260.    random.shuffle(boxes)
    261.    boxGroups = splitIntoGroupsOf(8, boxes)
    262. 
    263.    drawBoard(board, coveredBoxes)
    264.    for boxGroup in boxGroups:
    265.        revealBoxesAnimation(board, boxGroup)
    266.        coverBoxesAnimation(board, boxGroup)
    267. 
    268.
    269. def gameWonAnimation(board):
    270.    # flash the background color when the player has won
    271.    coveredBoxes = generateRevealedBoxesData(True)
    272.    color1 = LIGHTBGCOLOR
    273.    color2 = BGCOLOR
    274. 
    275.    for i in range(13):
    276.        color1, color2 = color2, color1 # swap colors
    277.        DISPLAYSURF.fill(color1)
    278.        drawBoard(board, coveredBoxes)
    279.        pygame.display.update()
    280.        pygame.time.wait(300)
    281. 
    282.
    283. def hasWon(revealedBoxes):
    284.    # Returns True if all the boxes have been revealed, otherwise False
    285.    for i in revealedBoxes:
    286.        if False in i:
    287.            return False # return False if any boxes are covered.
    288.    return true
    289. 
    290.
    291. if __name__ == '__main__' :



