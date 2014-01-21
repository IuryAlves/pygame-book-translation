12 http://inventwithpython.com/pygame

	7. while True: # loop principal do jogo
	8.	for event in pygame.event.get():

A linha 8 é um loop `for` que irá iterar sobre toda a lista de objetos event que é retornado por `pygame.event.get()`.Em cada iteração atráves
do loop `for`, uma variável chamada `event` será atribuída ao valor do próximo objeto event na lista.A lista de objetos Event retornada de 
`pygame.event.get()` será na ordem em que os eventos acontecem.Se o usuário clicou o mouse e pressionou uma tecla, o objeto Event para o clique
do mouse deve ser o primeiro item na lista e o objeto Event para o pressionar do teclado deve ser o segundo.Se nenhum evento acontecer, então
`pygame.event.get()` irá retornar uma lista vazia.

#### O QUIT Event e a função pygame.quit()

	9. 		if event.type == QUIT:
	10.			pygame.quit()
	11.			sys.exit()


Objetos Event possuem uma variável membro(também chamada de atributo ou propiedade) nomeada type, que nos informa que tipo o objeto representa
.O Pygame possui uma constante para cada um dos tipos possíveis no módulo pygame.locals.A linha 9 verifica se o tipo do objeto Event é igual
a constante QUIT.Lembre-se desde que nós usamos `from pygame.locals import *` como forma de import, nós apenas que digitar QUIT ao invés de 
pygame.locals.QUIT.

Se o objeto Event é um quit event, então as funções  `pygame.quit()` e `sys.exit()`são chamadas.A função `pygame.quit()` é o oposto da função
`pygame.init()`: ela executa código que desativa a biblioteca do Pygame.Seus programas devem sempre chamar `pygame.quit()` antes de chamar
`sys.exit()` para encerrar seu programa.Normalmente realmente não importa como o Python fecha quando um programa termina.Mas existe um bug no
IDLE que provoca que ele travese um programa com Pygame encerrar antes que pygame.quit() for chamado.

Desde que nós temos nenhuma instrução `if` que executa código para outros tipos de objeto Event, não existe código que manipula os 
eventos quando o usuário clica com o mouse, pressiona alguma tecla, ou provoque que qualquer outro tipo de objetos Event seja criado.O 
usuário pode fazer coisas para criar esses objetos Event, mas isso não modificará em nada o programa porque o programa não tem nenhum 
tipo de código para manipulação de eventos.Após o loop `for` na linha 8 completar a manipulação de todos os objetos Event que retornaram de 
pygame.event.get(), a execução do programa continua na linha 12.

	12.		pygame.display.update()	

> Mande questões por E-mail para o autor : al@inventwithpython.com
