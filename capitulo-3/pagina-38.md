38 http://inventwithpython.com/pygame

    122.        FPSCLOCK.tick(FPS)
    123.
    124.
    125. def generateRevealedBoxesData(val):
    126.    revealedBoxes = []
    127.    for i in range(BOARDWIDTH):
    128.        revealedBoxes.append([val] * BOARDHEIGHT)
    129.    return revealedBoxes
    130. 
    131.
    132. def getRandomizedBoard():
    133.    # Get a list of every possible shape in every possible color.
    134.    icons = []
    135.    for color in ALLCOLORS:
    136.        for shape in ALLSHAPES:
    137.            icons.append( (shape, color) )
    138. 
    139.    random.shuffle(icons) # randomize the order of the icons list
    140.    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many
    icons are needed
    141.    icons = icons[:numIconsUsed] * 2 # make two of each
    142.    random.shuffle(icons)
    143. 
    144.    # Create the board data structure, with randomly placed icons.
    145.    board = []
    146.    for x in range(BOARDWIDTH):
    147.        column = []
    148.        for y in range(BOARDHEIGHT):
    149.            column.append(icons[0])
    150.            del icons[0] # remove the icons as we assign them
    151.        board.append(column)
    152.    return board
    153. 
    154.
    155. def splitIntoGroupsOf(groupSize, theList):
    156.    # splits a list into a list of lists, where the inner lists have at
    157.    # most groupSize number of items.
    158.    result = []
    159.    for i in range(0, len(theList), groupSize):
    160.        result.append(theList[i:i + groupSize])
    161.    return result
    162. 
    163.
    164. def leftTopCoordsOfBox(boxx, boxy):
    165.    # Convert board coordinates to pixel coordinates
    166.    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN

> Mande dúvidas por E-mail para: al@inventwithpython.com

