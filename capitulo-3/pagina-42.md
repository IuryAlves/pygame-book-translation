muito melhor, especialmente porque nós podemos usar o valor 40 para algo a mais do que o tamanho dos 'white boxes', e mudar o valor 40 pode acidentalmente causar bugs no seu programa.

Segundo, torna o código mais legível, Vá para a próxima seção e veja a linha 18.Nessa linha o valor da constante XMARGIN é configurado, que é a quantidade de pixels que estão no lado do quadro inteiro.É uma expressão complicada, mas você pode cuidadosamente entender o que significa.A linha 18 está assim:

    XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)