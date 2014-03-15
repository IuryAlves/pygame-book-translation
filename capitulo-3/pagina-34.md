34 http://inventwithpython.com/pygame

    2 b
    2 c
    3 a
    3 b
    3 c
    4 a
    4 b
    4 c
    >>>


Em muitos momentos do código do jogo da memória, nós precisamos iterar em toda possível combinação das coordenadas X e Y no quadro.Nós usaremos `for` loops aninhados para ter certeza de obter cada combinação possível.Perceba que o `for` interno do loop (o `for` dentro do loop `for`)  irá executar todas as sua iterações antes que o for externo passe para a sua próxima iteração.Se nós invetermos a ordem dos loops `for`, os mesmos valores serão impressos, mas eles serão impressos em ordem diferente.Digite o seguinte código no interpretador interativo, e compare a ordem que os valores são impressos com a ordem no exemplo anterior:

    >>> for y in ['a', 'b', 'c']:
    ...     for x in [0, 1, 2, 3, 4]:
    ...         print(x, y)

    0 a
    1 a
    2 a
    3 a
    4 a
    0 b
    1 b
    2 b
    3 b
    4 b
    0 c
    1 c
    2 c
    3 c
    4 c
    >>>

#### Código fonte do jogo da memória

Esse código fonte pode ser baixado em http://invpy.com/memorypuzzle.py .

Vá em frente e digite o programa inteiro dentro do editor IDLE, e salve-o como pemorypuzzle.py, e execute-o.Se você tiver alguma mensagem de erro, olhe para o número da linha que é mencionada na


> Mande dúvidas por E-mail para o autor: al@inventwithpython.com
