20 http://inventwithpython.com/pygame


<table>
	<tr>
		<td>Nome do atributo</td>
		<td>Descrição</td>
	</tr>
	<tr>
	<td>myRect.left</td>
	<td>O valor inteiro da coordenada X do lado esquerdo do retângulo</td>
	</tr>
	<tr>
	<td>myRect.right </td>
	<td>O valor inteiro da coordenada X do lado direito do retângulo</td>
	</tr>
	<tr>
	<td>myRect.top</td>
	<td>O valor inteiro da coordenada Y do lado de cima do retângulo</td>
	</tr>
	<tr>
	<td>myRect.bottom</td>
	<td>O valor inteiro da coordenada Y do lado de baixo do retângulo</td>
	</tr>
	<tr>
	<td>myRect.centerx</td>
	<td>O valor inteiro da coordenada X do centro do retângulo</td>
	</tr>
	<tr>
	<td>myRect.centery</td>
	<td>O valor inteiro da coordenada Y di centri do retângulo</td>
	</tr>
	<tr>
	<td>myRect.width</td>
	<td>O valor inteiro da largura do retângulo</td>
	</tr>
	<tr>
	<td>myRect.height</td>
	<td>O valor inteiro da altura do retângulo</td>
	</tr>
	<tr>
	<td>myRect.size</td>
	<td>Uma tupla de dois inteiros: (largura, altura)</td>
	</tr>
	<tr>
	<td>myRect.topleft</td>
	<td>Uma tuppla de dois inteiros: (esquerda, cima)</td>
	</tr>
	<tr>
	<td>myRect.topright</td>
	<td>Uma tupla de dois inteiros: (direita, cima)</td>
	</tr>
	<tr>
	<td>myRect.bottomleft</td>
	<td>Uma tupla de dois inteiros: (esquerda, baixo)</td>
	</tr>
	<tr>
	<td>myRect.bottomright</td>
	<td>Uma tupla de dois inteiros: (direita, baixo)</td>
	</tr>
	<tr>
	<td>myRect.midleft</td>
	<td> Uma tupla de dois inteiros: (esquerda, centro)</td>
	</tr>
	<tr>
	<td>myRect.midright</td>
	<td>Uma tupla de dois inteiros: (direita, centro)</td>
	</tr>
	<tr>
	<td>myRect.midtop</td>
	<td>Uma tupla de dois inteiros: (centerx, cima)</td>
	</tr>
	<tr>
	<td>myRect.midbottom</td>
	<td>Uma tupla de dois inteiros: (centerx, baixo)</td>
	</tr>
</table>


#### Funções primitivas de desenho


O Pygame fornece muitas funções para desenhar diferentes formas em um objeto Surface.Essas formas como retângulos, círculos, elipses, linhas, ou pixels
são chamadas primitivas de desenho.Abra o editor de arquivos IDLE e digite o seguinte programa e salve-o como drawing.py.

	1. import pygame, sys
	2. from pygame.locals import *

> Mande questões por E-mail para o autor: al@inventwithpython.com
