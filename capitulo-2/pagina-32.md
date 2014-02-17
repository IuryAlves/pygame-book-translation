32 http://inventwithpython.com/pygame

Para parar de tocar a música de fundo imediatamente, chame a função `pygame.mixer.music.stop()`.Essa função não possui argumentos.

Aqui está um exemplo de código que possui métodos e funções de som.

    # loading and playing a sound effect:
    soundObj = pygame.mixer.Sound('beepingsound.wav')
    soundObj.play()

    # Loading and playing background music:
    pygame.mixer.music.load('backgroundmusic.mp3')
    pygame.mixer.music.play(-1, 0.0)
    # ... some more of your code goes here
    pygame.mixer.music.stop()


#### Sumário

Esse capítulo cobriu o básico de desenvolver jogos gráficos com Pygame.É claro, apenas ler essas funções provavelmente não é o suficiente para te ajudar a aprender como desenvolver jogos.O resto dos capítulos nesse livro irá focar no código fonte de jogos curtos e completos.Isso lhe dará uma ideia de como um jogo completo funciona, então você pode então ter ideias de como desenvolver seus própios jogos.

Diferente do livro "Invent Your Own Computer Games with Python", esse livro assume que você conhece o básico de programação em Python.Se você tiver problemasem lembrar como variáveis, funções, laços, instruções if-else, e condições funcionam, você pode entender esse conceitos olhando como essas instruções se comportam nos códigos desse livro.Mas se mesmo assim, você ainda tiver problemas, você pode ler o livro "Invent with Python" (destinado para pessoas que são completamente novas no mundo da programação) de graça em http://iventwithpython.com.

> Mande questões por E-mail para o autor: al@inventwithpython.com
> 
> 