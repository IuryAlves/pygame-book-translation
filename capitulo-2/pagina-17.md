Capítulo 2 - Noções básicas de Pygame 17

#### Cores transparentes

Quando você olha através de uma janela de vidro que possui tinta vermelha, todas as cores através da janela possuem uma sombra vermelha.Você pode imitar esse efeito usando um quarto valor inteiro de 0 até 255 para os valores de suas cores.

Esse valor é conhecido como *alpha value*. Ele mensura o quão opaco (isso é, não transparente) uma cor é.Normalmente quando você desenha um pixel em um objeto Surface, a nova cor substituí completamente qualquer cor que esteja lá.Mas cores com *alpha value*, você pode apenas adicionar um tom de cor
para a cor que já existe.

Por exemplo, essa tupla de três inteiros é a cor verde: (0, 255, 0).Mas se adicionassemos uma quarta cor para o *alpha value* , nós podemos tornar a cor verde meio transparente: (0, 255, 0, 128).Um *alpha value* de 255 é completamente opaco(isso é, não possui transparência) .As cores (0, 255, 0) e (0, 255, 0 , 255) são exatamente iguais.Um *alpha value* de 0 significa que a cor é completamente transparente.Se você desenhar qualquer cor que possui um *alpha value* de 0 em um objeto Surface, ele não terá mudança, porque a cor é completamente transparente e invisível.

Para poder desenhar cores transparentes, você precisa criar um objeto Surface com o método `convert_alpha()` .Por exemplo, o seguinte código cria um objeto Surface em que cores transparentes podem ser desenhadas.

	anotherSurface = DISPLAYSURF.convert_alpha()


Uma vez que algo foi desenhado no objeto Surface que está guardado em `anotherSurface`, então `anotherSurface` pode ser `blitted` (isso é, copiado) para DISPLAYSURF para poder aparecer na tela. (Veja a seção "Desenhando imagens com pygame.image.load() e blit()" nesse capítulo).

É  importante notar que você não pode usar cores transparentes em objetos Surface que não foram retornados de `convert_alpha()`, incluindo o display Surface que foi retornado de `pygame.display.set_mode()`.

Se nós criássemos  uma tupla de cor para desenhar o Legendário invisível Unicórnio rosa, nós deveríamos usar (255, 192, 192, 0), o que é totalmente  invísivel do mesmo jeito que qualquer outra cor que possui 0 como *alpha value*.
