Capítulo 2 - Noções básicas de Pygame 21

	3.
	4. pygame.init()
	5.
	6. # set up the window
	7. DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
	8. pygame.display.set_caption('Drawing')
	9.
	10. #cores
	11. BLACK = (0, 0, 0)
	12. WHITE = (255, 255, 255)
	13. RED   =  (255, 0, 0)
	14. GREEN = (0, 255, 0)
	15. BLUE  = (0, 0, 255)
	16.
	17. #desenha no objeto Surface
	18. DISPLAYSURF.fill(WHITE)
	19. pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))
	20. pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), 120, 60), 4)
	21. pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
	22. pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
	23. pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
	24. pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
	25. pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
	26.
	27. pixObj = pygame.PixelArray(DISPLAYSURF)
	28. pixObj[480][380] = BLACK
	29. pixObj[482][382] = BLACK
	30. pixObj[484][384] = BLACK
	31. pixObj[486][386] = BLACK
	32. pixObj[488][388] = BLACK
	33. del pixObj
	34.
	35. #executa o loop do jogo
	36. while True:
        37.     for event in pygame.event.get():
        38.             if event.type == QUIT:
        39.                     pygame.quit()
        40.                     sys.exit()
        41.     pygame.display.update()

Quando o programa é executado, a seguinte janela é mostrada até que o usuário
feche janela
	
