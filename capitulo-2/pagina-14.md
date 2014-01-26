14 http://inventwithpython.com/pygame

O framework Pygame frequentemente representa as coordenadas cartesianas como uma tupla de dois inteiros, tal coo (4,0) ou (2,2).O primeiro inteiro
é a coordenada X e o segundo é a coordenada Y. (coordenadas cartesianas são explicadas detalhadamente no capítulo 12 de "Invent Your Own Computer
Games with Python" em http://invpy.com/chap12)

#### Um lembrete sobre Funções, Métodos, Funções Construtoras, e Funções em Módulos (e a Diferença entre eles) 

Funções e métodos são quase a mesma coisa.Ambos são chamados para executar código.A diferença entre função e método é que um método sempre estará
ligado ao seu objeto.Usualmente objetos mudam algo de um objeto em particular (você pensar no objeto anexado como uma espécie de argumento permanente
passado para o método).

Isso é uma chamada de função de uma função chamada `foo()`:

	foo()


Isso é uma chamada de método de um método que também se chama foo(), o qual está ligado com um objeto guardado em uma variável chamada `duckie` :

	duckie.foo()

Uma chamada para uma função dentro de um módulo pode se parecer com uma chamada de um método.Para perceber a diferença, você precisa olhar para o primeiro
nome e verificar se é um nome de um módulo ou de uma variável que contém um objeto.Você pode perceber que `sys.exit()` é uma chamada de função dentro
de um módulo, porque no topo do programa existe uma instrução `import` como `import sys`.

Uma função construtora é igual a uma função normal, exceto que o seu valor de retorno é um novo objeto.Apenas olhando no código fonte, uma 
função e uma função construtora são iguais.Funções construtoras (também chamadas de construtoras) são apenas uma convenção de nome usadas em funções
que retornam um novo objeto.Mas usualmente funções construtoras começam com uma letra maiúscula.É por isso que quando você escreve seus programas, seus
nomes de funções devem começar com uma letra minúscula.

Por exemplo, `pygame.Rect()` e `pygame.Surface()` são funções construtoras dentro do módulo pygame que retornam um novo objeto Rect e objeto Surface
respectivamente (esses objetos serão explicados depois).

Aqui está um exemplo de chamada de função, chamada de método, e uma chamada para uma função dentro de um módulo:

	import whammy
	fizzy()

> Mande questões por E-mail para o autor : al@inventwithpython.com
