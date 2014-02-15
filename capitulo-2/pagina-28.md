28 http://inventwithpython.com/pygame

#### Desenhando imagens com pygame.image.load() e blit()

As funções de desenho são simples se você quer desenhar simples formas na tela, mas muitos jogos possuem imagens(também chamadas de sprites).O Pygame consegue carregar imagens em objetos Surface a partir de arquivos PNG, JPG, GIF e BPM.As diferenças entre esses formatos de imagens é descrito em http://invpy.com/formats 

A imagem do gato foi guardada em um arquivo chamado cat.png.Para carregar essa imagem a string 'cat.png' é passado para a função `pygame.image.load()`.A chamada para a função `pygame.image.load()` irá retornar um objeto Surface que permite que imagens possam ser desenhadas nele.o objeto Surface será um objeto separado do objeto display Surface, então nós precisamos copiar o objeto Surface para o objeto display Surface.*Blitting* é o mesmo que desenhar os conteúdos  de um objeto Surface em outro.É feito usando o método `blit()` do objeto Surface.

Se você obter uma mensagem de erro como `pygame.error: Couldn't open cat.png` quando você chamar `pygame.image.load()`, significa que o pygame não encontrou a imagem, tenha certeza de que a imagem está na mesma pasta que o arquivo catanimation.py.

	39.		DISPLAYSURF.blit(catImg, (catx, caty))

A linha 39 do programa usa o método `blit()` para copiar `catImg` para `DISPLAYSURF`.
O método `blit()` possui dois parâmetros.O primeiro é o objeto Surface fonte, que será copiado para o objeto DISPLAYSURF.O segundo parâmetro é uma tupla de dois inteiros para os valores de X e Y do canto superior esquerdo onde a imagem deve ser copiada.

Se catx e caty forem ajustados para 100 e 200 e a largura de catImg for 125 e a altura for 79, essa chamada para o método `blit()` deverá copiar a imagem para DISPLAYSURF e o canto superior esquerdo seria as coordenadas XY (100, 200) e o canto inferior direito estaria nas coordenadas XY (225, 279).

Perceba que você não pode copiar uma superfície se ela estiver 'bloqueada'(como quando o objeto pixelArray foi criado e não foi deletado.)

O que o restante do loop do jogo faz é apenas mudar as variáveis catx, caty e direction para que o cato possa se mover na janela.Também existe uma chamada para `pygame.event.get()` para lidar com o evento `QUIT`.

#### Fontes

Se você quer desenhar texto na tela, você pode fazer diversas chamadas para `pygame.draw.line()` para desenhar as linhas de cada letra.Isso pode gerar muita dor de cabeça para poder digitar cada uma dessas chamadas.