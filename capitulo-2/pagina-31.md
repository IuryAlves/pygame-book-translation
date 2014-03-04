Capítulo 2 - Noções básicas de Pygame 31

`pygame.draw.lines()`, exceto que essas funções irão desenhar linhas com anti-aliasing.

#### Tocando Sons

Tocar sons que são guardados em arquivos de som é tão simples quanto mostrar imagens.Primeiro, você precisa criar um objeto `pygame.mixer.Sound` (o qual nós chamaremos de objetos Sound), chamando a função construtora `pygame.mixer.Sound()`. Essa função recebe uma string como parâmetro, que é o nome do arquivo de som.O Pygame pode carregar arquivos WAV, MP3, OGG.As diferenças entre esses arquivos de som é explicado em http://invpy.com/formats.

Para tocar um som, chame o método do objeto Sound `play()`.Se você que parar o som chame o método `stop()`, o método `stop()` não possui parâmetros.
Aqui está um código de exemplo:

    soundObj = pygame.mixer.Sound('beeps.wav')
    soundObj.play()
    import time
    time.sleep(1) # wait and let the sound play for 1 second
    soundObj.stop()


Você pode baixar o arquivo beeps.wav em http://invpy.com/beeps.wav.

A execução do programa continua imediatamente após o método `play()` for chamado.O método não espera até o som terminar para ir para a próxima linha de código.

Os objetos Sound são bons para tocar efeitos sonoros quando o jogador leva dano,ataca, ou coleta uma moeda.Mas seus jogos podem ser tornar melhores se eles possuírem música de fundo tocando independetemente do que está acontecendo no jogo.O pygame pode apenas carregar um arquivo de música de fundo, para tocar, por vez.Para carregar uma música de fundo, chame a função `pygame.mixer.music.load()` e passe uma string como parâmetro com o local do arquivo para ser carregado.Esse arquivo pode ser no formato WAV, MP3, ou MIDI.

Para começar a tocar um som como música de fundo, chame a função `pygame.mixer.music.play(-1, 0.0)`.O parâmetro -1 faz a música de fundo reiniciar quando ela chegar ao final.Se você configurar para um inteiro igual a zero ou maior, então a música irá executar um número de vezes ao invés de repetir até o jogo ser encerrado.Se você passar um inteiro grande ou um float, a música irá começar a tocar a partir daquele tempo no arquivo de som.Por exemplo se voc passar 13.5 para o segundo parâmetro, o som irá começar a tocar a partir dos 13.5 segundos da música.
