Capítulo 2 - Noções básicas de Pygame 19

2. A coordenada Y no topo do canto esquerdo.
3. A largura (em pixels) do retângulo.
4. Então a altura (em pixels) do retângulo.

O segundo jeito é usando o objeto pygame.Rect, que nós iremos chamar de objetos Rect.Por exemplo, o código abaixo cria um objeto Rect com o canto
superior esquerdo em (10, 20), e com 200 pixels de largura e 300 pixels de altura:

	>>> import pygame
	>>> spamRect = pygame.Rect(10, 20, 200, 300)
	>>> spamRect == (10, 20, 200, 300)
	True


A vantagem disso é que o objeto Rect automaticamente calcula as coordenadas para os recursos do retângulo.Por exemplo, se você precisar saber a coordernada
X da ponta direita de um objeto pygame.Rect que guardamos na variável spamRect, você pode acessar o atributo `right` do objeto Rect.

	>>> spamRect.right
	210

O objeto Rect calcula automaticamente que se a extremidade direita está na coordenada X de valor 10 e o retângulo tem 200 pixels de largura,então a 
margem direita deve estar na coordenada X 210.Se você renomear o atributo right, todos os outros atributos serão automaticamente recalculados:


	>>> spamRect.right = 350
	>>> spamRect.left
	150

Aqui está uma lista de todos os atributos  que o objeto pygame.Rect fornece( em nosso exemplo, a variável onde o objeto Rect foi guardado é chamada de myRect):
