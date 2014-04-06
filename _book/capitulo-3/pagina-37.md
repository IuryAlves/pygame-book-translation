Capítulo 3 - jogo da Memória 37

    83.     if boxx != None and boxy != None:
    84.         # The mouse is currently over a box.
    85.         if not revealedBoxes[boxx][boxy]:
    86.             drawHighlightBox(boxx, boxy)
    87.         if not revealedBoxes[boxx][boxy] and mouseClicked:
    88.             revealBoxesAnimation(mainBoard, [(boxx, boxy)])
    89.             revealedBoxes[boxx][boxy] = True # set the box as "revealed"
    90.             if firstSelection == None: # the current box was the first
    box clicked
    91.                 firstSelection = (boxx, boxy)
    92.             else: # the current box was the second box clicked
    93.                 # Check if there is a match between the two icons.
    94.                 icon1shape, icon1color = getShapeAndColor(mainBoard,
    firstSelection[0], firstSelection[1])
    95.                 icon2shape, icon2color = getShapeAndColor(mainBoard,
    boxx, boxy)
    96.
    97.                 if icon1shape != icon2shape or icon1color !=
    icon2color:
    98.                     # Icons don't match. Re-cover up both selections.
    99.                     pygame.time.wait(1000) # 1000 milliseconds = 1 sec
    100.                    coverBoxesAnimation(mainBoard,
    [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
    101.                    revealedBoxes[firstSelection[0]][firstSelection[1]] = False
    102.                    revealedBoxes[boxx][boxy] = False
    103.                elif hasWon(revealedBoxes): # check if all pairs found
    104.                    gameWonAnimation(mainBoard)
    105.                    pygame.time.wait(2000)
    106. 
    107.                    # Reset the board
    108.                    mainBoard = getRandomizedBoard()
    109.                    revealedBoxes = generateRevealedBoxesData(False)
    110. 
    111.                    # Show the fully unrevealed board for a second.
    112.                    drawBoard(mainBoard, revealedBoxes)
    113.                    pygame.display.update()
    114.                    pygame.time.wait(1000)
    115. 
    116.                    # Replay the start game animation.
    117.                    startGameAnimation(mainBoard)
    118.                firstSelection = None # reset firstSelection variable
    119. 
    120.    # Redraw the screen and wait a clock tick.
    121.    pygame.display.update()

