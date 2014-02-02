20 http://inventwithpython.com/pygame

Nome do atributo         Descrição
---------------------------------------------------------------------------------------------

myRect.left              O valor inteiro da coordenada X do lado esquerdo do retângulo.

myRect.right             O valor inteiro da coordenada X do lado direito do retângulo.

myRect.top               O valor inteiro da coordenada Y do lado de cima do retângulo.

myRect.bottom            O valor inteiro da coordenada Y do lado de baixo do retângulo.

myRect.centerx           O valor inteiro da coordenada X do centro do retângulo.

myRect.centery           O valor inteiro da coordenada Y di centri do retângulo.

myRect.width             O valor inteiro da largura do retângulo.

myRect.height            O valor inteiro da altura do retângulo.

myRect.size              Uma tupla de dois inteiros: (largura, altura).

myRect.topleft           Uma tuppla de dois inteiros: (esquerda, cima).

myRect.topright          Uma tupla de dois inteiros: (direita, cima).

myRect.bottomleft        Uma tupla de dois inteiros: (esquerda, baixo).

myRect.bottomright       Uma tupla de dois inteiros: (direita, baixo).

myRect.midleft           Uma tupla de dois inteiros: (esquerda, centro).

myRect.midright          Uma tupla de dois inteiros: (direita, centro).

myRect.midtop            Uma tupla de dois inteiros: (centerx, cima).

myRect.midbottom         Uma tupla de dois inteiros: (centerx, baixo).


#### Funções primitivas de desenho


O Pygame fornece muitas funções para desenhar diferentes formas em um objeto Surface.Essas formas como retângulos, círculos, elipses, linhas, ou pixels
são chamadas primitivas de desenho.Abra o editor de arquivos IDLE e digite o seguinte programa e salve-o como drawing.py.

	1. import pygame, sys
	2. from pygame.locals import *

> Mande questões por E-mail para o autor: al@inventwithpython.com
