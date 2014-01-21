10 http://inventwithpython.com/pygame

lembre-se de passar uma tupla de dois inteiros para o `set_mode()`, não apenas dois inteiros.O jeito correto de chamar a função é assim: 
`pygame.display.set_mode( (400, 300))`.Uma chamada para a função como `pygame.display.set_mode(400, 300)` causará um erro que se parece assim:
`TypeError: argument 1 must be 2-item sequence, not int`.

	6. pygame.display.set_caption('Olá Mundo!')

A linha 6 coloca o texto de título que irá aparecer no topo da janela, chamando a função `pygame.display.set_caption()`.A conteúdo da string 'Olá
Mundo!' é passada para a chamada da função para fazer o texto aparecer como o título:

#### Loops do jogo e states do jogo

	7. while True: #loop principal do jogo
	8.	for event in pygame.event.get():

A linha 7 é um while que tem uma simples condição com o valor True.Isso siginifica que ela nunca irá parar, sendo que sua condição nunca será
False.O único jeito de parar a execução do programa será se uma instrução de  `break` for executado(o que coloca a execução na primeira linha após
o loop) ou `sys.exit()` (o que termina o programa).Se um loop como esse estivesse dentro de uma função, uma instrução de  `return` também irá colocar a execução para fora do loop(e a função também).

Todos os jogos nesse livro possuem o loop `while True` contendo um comentário dizendo "loop principal do jogo".Um loop do jogo(também chamado) loop principal) é um loop onde o código realiza três coisas:

1. Manipula eventos

2. Atualiza o estado do jogo
 
3. Desenha o estado do jogo na tela.

O Estado do jogo é uma forma simples de se referir a um conjunto de valores para todas as variáveis do programa.Em muitos jogos, o estado do jogo inclui os valores de variáveis que guardam a vida do jogador e sua posição, a vida e posição de todos os inimigos, que são desenhados em um quadro, o placar, ou de quem é o turno.Sempre que acontece algo como o jogador

> Mande questões por E-mail para o autor : al@inventwithpython.com
