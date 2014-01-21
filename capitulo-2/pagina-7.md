capítulo 2 - Noções básicas de Pygame


# Capítulo 2 - Noções básicas de Pygame

Do mesmo jeito que o Python vem com muitos módulos como random,math, ou time que fornece funções adicionais para seus programas, o framework do
Pygame inclui  módulos com funções para desenhar gráficos, tocar músicas, usar o input do mouse, e outras coisas.

Esse capítulo irá cobrir os módulos basicos e funções que o Pygame fornece e assume que você já sabe o básico de programação em Python.Se você
tem problemas com algum conceito de programação, você pode ler o livro "Invent Your Own Computer Games with Python" online em http://invpy.com/book.
Esse livro tem como foco os iniciantes em programação.

O livro "Invent with Python" também possui alguns capítulos falando sobre o Pygame.Você poder ler em http://invpy.com/chap17.

Uma vez que você aprende mais sobre o Pygame, voce pode ver outros módulos que o Pygame fornece na documentação online em http://pygame.org/docs.

#### GUI vcs. CLI

Os programas Python que você escreve com as funções internas apenas lidam com texto através das funções print() e input().Seu programa pode mos
trar texto na tela e permitir que o usuário digite texto a partir do teclado.Esse tipo de programa possui uma interface em linha de comando,
ou CLI(que é pronunciado como a primeira parte de "climb" e rima com "sky"). Esses programas são limitados porque não podem mostrar gráficos
,possuir cores, ou usar o mouse.Esses programas em CLI apenas recebem a entrada do teclado com a função input() mesmo que o usuário pressione
Enter antes do programa poder responder a entrada.Isso siginifica tempo-real(isso é, execute código sem esperar pelo usuário) jogos de ação
não podem fazer isso. (essa parte precisa de revisão =) )

Pygame fornece funções para criar seus programas com uma interface gráfica, ou GUI.Ao inveś de uma CLI baseada em texto, programas baseados em
interfaces gráficas podem mostrar uma janela com imagens e cores.

#### Código de um Olá Mundo com Pygame

Nosso primeiro programa feito com Pygame é um pequeno programa que cria uma janela que diz "Olá Mundo" e á faz aparecer na tela.Abra um novo
arquivo na janela do editor clicando em arquivo no menu do IDLE, e depois Nova Janela.Digite o seguinte código dentro do arquivo do  IDLE e
salve como blankpygame.py. Então execute o programa pressionando a tecla f5 ou selecionando Executar > Executar Modulo no menu no topo do editor


