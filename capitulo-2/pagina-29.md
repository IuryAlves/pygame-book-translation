Capítulo 2 - Noções básicas de pygame 29

para a função `pygame.draw.line()` e calcular todas as coordenadas XY, e provavelmente não ficaria tão bom.

![](imagens/imagem-29)

A mensagem acima deve realizar 40 chamadas para a função `pygame.draw.line()`.Ao invés disso, o Pygame fornece muitas funções simples para lidar com fontes e textos.Aqui está um simples programa usando as funções de desenho do pygame.Digite no editor de textos IDLE's e salve como fonttext.py:

	1. import pygame, sys 
	2. from pygame.locals import * 
	3.
	4.pygame.init() 
	5.DISPLAYSURF = pygame.display.set_mode((400, 300)) 
	6.pygame.display.set_caption('Hello World!') 
	7.
	8. WHITE = (255, 255, 255) 
	9. GREEN = (0, 255, 0) 
	10. BLUE = (0, 0, 128) 
	11.
	12. fontObj = pygame.font.Font('freesansbold.ttf', 32) 
	13. textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE) 
	14. textRectObj = textSurfaceObj.get_rect() 
	15. textRectObj.center = (200, 150) 
	16. 
	17. while True: # main game loop
	18. 	DISPLAYSURF.fill(WHITE)
	19. 	DISPLAYSURF.blit(textSurfaceObj, textRectObj) 
	20. 	for event in pygame.event.get(): 
	21. 		if event.type == QUIT: 
	22. 			pygame.quit() 
	23. 			sys.exit() 
	24. 	pygame.display.update() 


Existem seis passos para fazer o texto aparecer na tela:

1. Crie um objeto `pygame.font.Font`. (Como na linha 12)
2. Crie um objeto Surface com um texto nele, chamando a função `render()` do objeto Font (linha 13)
3. Crie um objeto Rect a partir do objeto Surface, chamando o método `get_rect()` (linha 14).Esse objeto terá a largura e a altura corretamente ajustadas pra o texto que foi renderizado, mas os atríbutos `top` e `left` serão 0.










