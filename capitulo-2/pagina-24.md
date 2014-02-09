24 http://inventwithpython.com/pygame

ainda podem ser chamadas, mas imagens como PNG ou JPG não podem ser desenhadas com o método `blit()`.(O método `blit` será explicado depois).

Se você quer saber se um objeto Surface está bloqueado, o método `get_locked()` irá retornar `True` se ele está bloqueado e `False` caso contrário.

O objeto PixelArray que é retornado por `pygame.PixelArray()` pode ter pixels indivíduais alterados acessando eles com dois indíces.Por exemplo, na linha 28, `pixObj[480][380] = BLACK` irá alterar o pixel na coordenada X 480 e Y 380 para preto(lembre-se que a variável BLACK guarda a tupla (0, 0, 0) ).

Para informar o Pygame que você terminou de desenhar pixels, delete o objeto PixelArray com a instrução `del`.Isso é o que a linha 33 faz.O ato de deleta o objeto PixelArray irá desbloquear o objeto Surface para que imagens possam ser desenhaadas novamente.Se você se esquecer de deleta o objeto PixelArray, na próxima vez em que você tentar copiar(isso é desenhar) uma imagem para o objeto Surface o programa irá gerar um erro que diz:
    "pygame.error: Surfaces must not be locked during blit". 

A função pygame.display.update()

Se você terminou de chamar as funções de desenho para fazer o objeto Surface se parecer do jeito que você deseja, você precisa chamar `pygame.display.update()` que irá fazer o objeto Surface aparecer na tela.

Uma coisa que você precisa lembrar é que `pygame.display.update()` apenas irá  fazer o `display Surface` (isso é, o objeto Surface que foi retornado da chamada de `pygame.display.set_mode()`) aparecer na tela, você precisa copiar para o objeto Surface com o método `blit()` (que será explicado posteriormente nesse capítulo).

#### Animação

Agora que nós sabemos como fazer o Pygame desenhar na tela, vamos aprender comofazer imagens animadas.Um jogo que apenas possui, imagems sem movimento é muito chato.(As vendas do meu jogo "Look at this Rock" foram desanimadoras.)Animar imagens é o resultado de desenhar imagens da tela, e então em um segundo desenhar uma imagem levemente diferente na tela.Imagine que a janela do programa possui 6 pixels de largura e 1 pixel de altura, com todos os pixelsexceto por um pixel preto em 4, 0. Que se parece com isso 

> Mande dúvidas por E-mail para o autor: al@inventwithpython.com 