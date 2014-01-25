Capítulo 2 - Noções basicas de Pygame 13

A linha 12 chama a função `pygame.display.update(), que desenha o objeto Surface retornado por `pygame.display.set_mode()` na tela(lembre-se
que nós á guardamos na variável DISPLAYSURF).Desde que o objeto Surface não mudou( por exemplo, por alguma função de desenho que serão explica
das mais tarde nesse capítulo), a mesma imagem preta é redesenhada na tela cada vez que `pygame.display.update()` é chamado.

Esse é o programa inteiro.Após a linha 12 for executada, o loop infinito inicia novamente do começo.Esse programa não faz nada além de fazer
uma janela preta aparecer na tela, constantemente verificando por um evento do tipo QUIT, e então redesenhar a inalterada janela preta na tela
novamente.Vamos aprender como fazer coisas interessantes aparecem na tela ao invés de apenas a cor preta aprendendo sobre pixels, objetos Surface,
objetos Color, objetos Rect e as funções de desenho do Pygame.


#### Coordenadas do pixel

A janela que o programa "Olá Mundo" criou é apenas composta de pequenos pontos quadrados na sua tela chamados pixels.Cada pixel inicia preto,
mas a sua cor pode ser mudada	
