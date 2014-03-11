muito melhor, especialmente porque nós podemos usar o valor 40 para algo a mais do que o tamanho dos 'white boxes', e mudar o valor 40 pode acidentalmente causar bugs no seu programa.

Segundo, torna o código mais legível, Vá para a próxima seção e veja a linha 18.Nessa linha o valor da constante XMARGIN é configurado, que é a quantidade de pixels que estão no lado do quadro inteiro.É uma expressão complicada, mas você pode cuidadosamente entender o que significa.A linha 18 está assim:

    XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)

Mas se a linha 18 não usasse constantes, ela ficaria assim:

    XMARGIN = int((640 – (10 * (40 + 10))) / 2)

Agora é imposível lembrar como exatamente o programa deveria ser.Esses números inexplicados no código fonte são chamados de números mágicos.Sempre que você perecber que você está usando números mágicos, você deve considerar lendo otrocar esses números mágicos por constantes.Para o interpretador python, ambas as linhas anteriores são iguais.Mas para um programador humano que está lendo o código fonte e tentando adivinhar como funciona, a segunda versão na linha 18 não faz muito sentido.Constantes realmente ajudam a legíbilidade do código.

É claro, você pode ir além e trocar esses números por constantes.Veja o seguinte código:

    ZERO = 0
    ONE = 1
    TWO = 99999999
    TWOANDTHREEQUARTERS = 2.75

Não escreva código assim, isso é muito idiota.

