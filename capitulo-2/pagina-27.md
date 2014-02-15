Capítulo 2 - Noções básicas de pygame 27

    47.     fpsClock.tick(FPS)

Veja o gato sendo animado !Esse programa será um sucesso comercial bem maior que que o meu jogo "Olhe para essa rocha 2: Uma rocha diferente".

#### Frames Por Segundo e Objetos pygame.time.Clock

O *frame rate* ou *refresh rate* é o número de imagens que o programa desenha por segundo, e é medido in *FPS* ou *frames por segundo*.(Em monitores de computador, o nome comum para FPS é hertz).Muitos monitores possuem um frame rate de 60 hertz, ou 60 frames por segundo.)Um *frame rate* muito baixo em jogo pode causar que o jogo fique lento.Se o programa possui muito código para executar para poder desenhar na tela, então a taxa do FPS cai.Mas os jogos nesse livro são simples o suficiente para que isso não seja um problema até mesmo para computadores antigos.

Um objeto pygame.time.Clock pode nos ajudar a ter certeza que o nosso programa executa até um determinado número máximo de FPS.Esse objeto Clock irá garantir que o nosso programa não execute muito rápido, colocando pequenas pausas em cada iteração do loop do jogo.Se não tivéssemos essas pausas, nosso jogo executaria o mais rápido possível.Isso é frequentemente muito rápido para o jogador, e como os computadores tendem a ser cada vez mais rápidos, o jogo irá rodar mais rápido também.Uma chamada para o método `tick()`  de um objeto `Clock` no loop do jogo pode nos dar a certeza de que o jogo execute na mesma velocidade não importando a velocidade do computador.O objeto Clock é criado na linha 7 do programa catanimation.py

    7. fpsClock = pygame.time.Clock()

O método `tick()`  do objeto `Clock` deve ser chamado bem perto do fim do loop do jogo , após a chamada para `pygame.display.update()`.O tamanho da pausa é calculado baseado em o quão longo foi a ultima chamada para o método `tick()`, que deve ter sido colocado no fim da iteração do loop anterior.(A primeira vez que o método `tick()` é chamado, ele não realmente pausa o jogo.)No programa de animação, ele é executado na linha 47 como a ultima instrução do loop do jogo.

Tudo o que você precisa saber é que você deve chamar o método `tick()` apenas uma vez por iteração no fim da iteraçã .Usualmente é logo após a chamada para `pygame.display.update()`.

    47. fpsClock.tick(FPS)
    

Tente modificar a constante FPS para executar o mesmo programa em frenquências diferentes.Ajustando para um valor mais baixo fará o programa executar mais devagar.Ajustando para um valor mais alto fará o programa executar mais rápido.
