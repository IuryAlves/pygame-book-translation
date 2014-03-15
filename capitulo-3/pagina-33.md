# Capítulo 3 - Jogo da memória

![](imagens/imagem-33.png)

#### Como jogar o jogo da memória

No jogo da memória, muitos icones são cobertos com caixas brancas.Existem dois de cada ícone.O jogador pode clicar em duas caixas para ver o que está debaixo delas.Se os ícones forem iguais, então esses ícones continuaram descobertos.O jogador ganha quando todas as caixas no quadro forem descobertas.Para dar ao jogador uma ajuda, no ínicio dos jogo as caixas são todas descobertas rapidamente.

#### Loops for aninhados

Um conceito que você verá no jogo da memória( e em muitos jogos desse livro) é usar um loop `for` dentro de outro loop `for`.Esses loops são chamados de loops `for` aninhados.loops `for` aninhados são bons para verificar cada possível combinação em duas listas.Digite o seguinte código no interpretador interativo:

    >>> for x in [0, 1, 2, 3, 4]:
    ...     for y in ['a', 'b', 'c']:
    ...         print(x, y)
    ...
    0 a
    0 b
    0 c
    1 a
    1 b
    1 c
    2 a



