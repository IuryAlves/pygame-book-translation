Capítulo 2 - Noções básicas do Pygame

A linha 1 é uma simples instrução de `import` que importa os módulos  pygame e sys, para que seu programa possa usar suas funções.Todas as funções
do Pygame que lidam com gráficos, som, e outros recursos que o Pygame fornece estão no módulo Pygame.

Note que quando você importa o módulo pygame, você automaticamente importa todos os módulos que estão no módulo do pygame,como o pygame.images
e pygame.mixer.music .Não existe a necessidade de importar esses sub-módulos com imports adicionais.

	2. from pygame.locals import *

Linha 2 também é uma instrução de  `import`.Entretanto, ao invés do `import` no formato nomedomódulo, é usado o formato `from nomedomódulo import *` .
Normalmente se você quer chamar uma função que está em um módulo, você precisa usar o formato nomedomódulo.nomedafuncao() após importar o mó
dulo.Entretanto com `from nomedomódulo import *`, você pode pular o trecho nomedomódulo. e simplesmente usar nomedafuncao() (como as funções
internas do Python).

A razão que nós usarmos essa forma de `import` para `pygame.locals` é porque `pygame.locals` contém muitas constantes que são fáceis de identificar
como sendo do módulo  `pygame.locals` sem `pygame.locals`. na frente delas.Para todos os outros módulos, você geralmente deve usar o formato import
nomedomódulo. (Existe mais informação sobre por que usar em http://invpy.com/namespaces.)

	4. pygame.init()

A linha 4 é a chamada para a função `pygame.init()`, que sempre precisa ser chamada após importar o módulo pygame e antes de chamar qualquer outra
função do Pygame.Você não precisa saber oque essa função faz, você apenas precisa saber que ela precisa ser chamada antes, para que  muitas funções
do Pygame possam funcioanar.Se você ver uma mensagem de erro como `pygame.error: font not initialized` , verifique se você se esqueceu de chamar `pygame.init()`
no início de seu programa.

	5. DISPLAYSURF = pygame.display.set_mode((400, 300))


A linha 5 é uma chamada para a função `pygame.display.set_mode()`, que retorna o objecto `pygame.Surface` para a janela.(objetos do tipo Surface 
serão vistos mais tarde nesse capítulo.)
Perceba que nós passamos uma tupla de com dois inteiros para a função: (400, 300) . Essa tupla diz a função `set_mode()` como deixa a janela em
largura e altura em pixels. (400, 300) fará com que a janela possua 400 pixels de largura e 300 pixels de altura.

