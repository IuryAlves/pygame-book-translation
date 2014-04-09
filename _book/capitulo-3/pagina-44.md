44 http://inventwithpython.com/pygame

A instrução `assert` na linha 15 garante que a largura e altura que nós selecionamos irá resultar em um número par de caixas(desde que nós temos pares de ícones no jogo). Em uma instrução `assert` existem três partes: a palavra reservada `assert`, uma expressão que, se for falsa, resulta no geramento de um erro. A terçeira parte(depois da vírgula) é uma string que aparece se o programa gera um erro por causa da asserção.

A instrução `assert` basicamente diz: "O programador afirma que a expressão precisa ser verdadeira", caso contrário gere um erro." Isso é uma boa maneira
de adicionar segurança em seu programa, para ter certeza de que ou a execução passa na asserção, para sabermos que o programa funciona como esperado.

#### Verificando se um número é par ou ímpar 

Se o produto da largura do quadro pela altura dividido por dois tiver um restante de zero (o operador módulo % mostra o restante entre dois números), então o número é par.Números pares divididos por dois sempre terão um restante igual a zero.Números impares divididos por dois sempre terão um restante igual a um.Isso é um bom truque para lembrar, se você precisar verificar se um número é par ou ímpar:

    >>> isEven = someNumber % 2 == 0
    >>> isOdd = someNumber % 2 != 0

No caso acima, se o inteiro `someNumber` for par, então `isEven` será `True`.Se for ímpar, então `isOdd` será `True`

#### Trave Antes e trave sempre!

Programas travando é algo ruim.Isso acontece quando seu programa possui algum erro no código e não pode continuar.Mas existem alguns caso em que travar seu programa cedo pode evitar bugs piores mais tarde.

Se os valores que escolhemos para `BOARDWIDTH`  e  para `BOARDHEIGHT` na linha 15 e 16 resultar em um quadro com um número impar de caixas (como se a largura for 3 e a altura for 5), então sempre deverá ter um ícone sobrando que não terá par.Isso pode causar um bug posterior no seu programa, e pode levar muito tempo debugando o programa para poder encontar o bug.De fato, apenas por diversão, comente a linha que possui a asserção e então configure o `BOARDWIDTH` e o `BOARDHEIGHT` para ter números impares.Quando você executar o programa, irá imediatamente aparecer um erro na linha 149 no memorypuzzle.py, que está dentro da função `getRandomizedBoard()`!

    Traceback (most recent call last):

Mande dúvidas por Email para o autor em: al@inventwithpython.com