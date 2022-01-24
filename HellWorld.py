from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from gameMenu import gameMenu
from fase1 import fase1
from fase2 import fase2

janela = Window(1440, 835)
janela.set_title("Hell World")

teclado = Window.get_keyboard()
mouse = Window.get_mouse()

modulo = 1
nivelDificuldade = 1

while True:
    etapaMenu = 1
    
    if modulo == 1:
        modulo, nivelDificuldade, etapaMenu = gameMenu(janela, teclado, mouse, modulo, nivelDificuldade, etapaMenu)

    if modulo == 2:
        modulo = fase1(janela, teclado, modulo, nivelDificuldade)

    if modulo == 3:
        modulo = fase2(janela, teclado, modulo, nivelDificuldade)

    janela.update()