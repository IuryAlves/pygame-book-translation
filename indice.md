# Índice

- Para quem esse livro é destinado?													 i
- Sobre o Livro																ii
- Capítulo 1 - Instalando o Python e o Pygame												 1
	O que Você Deve Saber Antes de Começar												 1
	Baixando e Instalando o Python													 1
	Instruções para Windows														 1
	Instruções para Mac OS X													 2
	Instruções para Ubuntu e Linux													 2
	Iniciando o Python														 2
	Instalando o Pygame														 3
	Como Usar Esse Livro														 4
	Os Programas Apresentados													 4
	Baixando Arquivos Gráficos e de Som												 4
	Número de Lihas e Espaços													 4
	Quebra automática de Texto Nesse Livro												 5
	Checando Seu Código Online													 6
	Mais Links Informativos em http://invpy.com											 6
- Capítulo 2 - Noções Básicas de Pygame													 7
	GUI vs. CLI															 7
	Código-fonte para Hello World com Pygame											 7
	Configurando um Progama do Pygame												 8
	Game Loops e Game States													10
	Objetos pygame.event.Event													11
	O Evento QUIT e a Função pygame.quit()												12
	Coordenadas do Pixel														13
	Um lembrete sobre Funções, Métodos, Funções Construtoras, e Funções em Módulos (e e a Diferença entre eles)			14
	Objetos de Superfície e a Janela												15
	Cores																16
	Cores Transparentes														17
	Objetos pygame.Color														18
	Objetos Rect															18
	Funções Primitivas de Desenho													20
	Objetos pygame.PixelArray													23
	A Função pygame.display.update()												24
	Animação															24
	Frames Por Segundo e Objetos pygame.time.Clock											27
	Desenhando Imagens com pygame.image.load() and blit()										28
	Fontes																28
	Anti-Aliasing															30
	Reprodução de Sons														31
	Sumário																32
- Capítulo 3 - Jogo da Memória														33
	Como Jogar o Jogo da Memória													33
	Loops for Aninhados														33
	Código-fonte do Jogo da Memória													34
	Créditos e Imports														42
	Números Mágicos são Ruins													42
	Checagens com Declarações assert												43
	Dizendo Se um Número é Par ou Ímpar												44
	Falha Precoce e Falha Frequente!												44
	Deixando o Código-fonte Bonito													45
	Usando Variáveis Constantes ao invés de Strings											46
	Certificando-se que Nós Temos Ícones o suficiente										47
	Tuplas vs. Listas, Imutáveis vs. Mutáveis											47
	Tuplas de Um Item Precisam de Uma Vírgula à Direita										48
	Conversão entre Listas e Tuplas													49
	A Declaração global, e Porque as Variáveis Globais são do Mal									49
	Estruturas de Dados e Listas 2D													51
	A Animação "Iniciar o Jogo"													52
	O Loop do Jogo															52
	O Evento Loop de Tratamento													53
	Checando em Qual Caixa o Cursor do Mouse Está											54
	Manipulando a Primeira Caixa Clicada												55
	Tratando Par de Ícones Incompatíveis												56
	Tratando se o Jogador Ganhou 													56
	Desenhando o Game State na Tela													57
	Criando a Estrutura de Dados "Caixas Reveladas"											58
	Criando a Estrutura de Dados do Quadro: Passo 1 - Obter Todos os Ícones Possíveis						59
	Passo 2 - Misturar e Truncar a Lista de Todos os Ícones										59
	Passo 3 - Posicionando os Ícones no Quadro											59
	Dividindo uma Lista em uma Lista de Listas											60
	Sistemas de Diferentes Coordenadas												61
	Convertendo de Coordenadas de Pixel para Coordenadas de Caixa									62
	Desenhando um Ícone, e Syntactic Sugar												63
	Obtendo a Forma e Cor dos Icones nos Espaços do Quadro com Syntactic Sugar							64
	Desenhando a Parte Coberta da Caixa												64
	Tratando as Animações de Revelando e Escondendo											65
	Desenhando o Quadro Inteiro													66
	Desenhando o Realçe														67
	A Animação de "Iniciar o Jogo"													67
	Revelando e Escondendo os Grupos de Caixas											68
	A Animação de "Você Venceu"													68
	Dizendo se o Jogador Ganhou													69
	Por que se Preocupar em ter uma Função main()?											69
	Por que se Preocupar com Legibilidade?												70
	Resumo, e uma sugestão de Hacking												74
- Capítulo 4 - Slide Puzzle														77
	Como Jogar Slide Puzzle														77
	Código-fonte para o Slide Puzzle												77
	Segundo Verso, Igual ao Primeiro												85
	Configurando os Botões 														89
	Sendo Esperto Usando Códigos Idiotas												87
	O Loop do Jogo Principal													88
	Clicando nos Botões														89
	Deslizando Ladrilhos com o Mouse												90
	Deslizando Ladrilhos com o Teclado												90
	Truque "Equal To One Of" com o Operador in											91
	WASD e Teclas de Seta														91
	Realmente fazendo o Azulejo Deslizar												92
	IDLE e Concluindo os Programas Pygame												92
	Checando por um Evento Específico, e Postando Eventos na Fila de Eventos da Pygame						92
	Criando a Estrutura de Dados do Quadro												93
	Não Rastreando a Posição em Branco												94
	Fazendo um Movimento por meio da Atualização da Estrutura de Dados do Quadro							94
	Quando NÃO Usar uma Asserção													95
	Obtendo um não tão aleatório Movimento												96
	Convertendo as Coordenadas dos Azulejos para Coordenadas de Pixel								97
	Convertendo de Coordenadas de Pixel para Coordenadas do Quadro									97
	Desenhando um Azulejo														97
	Fazendo o Texto Aparecer na Tela												98
	Desenhando o Quadro														99
	Desenhando a Borda do Quadro													99
	Desenhando os Botões														100
	Animando os Deslizes dos Azulejos												100
	O Método de Superfície copy()													101
	Criando um Novo Quebra-Cabeça													103
	Animando o Reset do Quadro													104