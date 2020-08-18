import pygame
from random import randrange

#Cores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


try:
    pygame.init()
except:
    print("O jogo não iniciou corretamente")

#Tamanho da tela
largura = 640
altura = 420
fps = 20

#Cobra
tamanho = 20

#Placar
placar = 60


relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

#Fonts
def texto(msg, cor, tam, x, y, modo):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    font_larg = texto1.get_width()
    font_alt = texto1.get_height()
    if modo == True:
        fundo.blit(texto1,[x, y])
    if modo == False:
        fundo.blit(texto1, [x - (font_larg//2), y - (font_alt // 2)])


def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(fundo, black, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, red, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    sair = True
    fimDeJogo = False
    pos_x = randrange(0,largura-tamanho, 20)
    pos_y = randrange(0,altura-tamanho -placar, 20)
    maca_x = randrange(0,largura-tamanho, 20)
    maca_y = randrange(0,altura-tamanho-placar, 20)
    velocidade_x = 0
    velocidade_y = 0
    velocidade = 20
    cobraXY = []
    cobraComp = 3
    pontos = 0
    while sair:
        while fimDeJogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimDeJogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimDeJogo = False
                        pos_x = randrange(0, largura - tamanho, 20)
                        pos_y = randrange(0, altura - tamanho - placar, 20)
                        maca_x = randrange(0, largura - tamanho, 20)
                        maca_y = randrange(0, altura - tamanho - placar, 20)
                        velocidade_x = 0
                        velocidade_y = 0
                        velocidade = 20
                        cobraXY = []
                        cobraComp = 3
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimDeJogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # x, y, x+X, y+Y
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 50 and y > ((altura // 2) - (altura // 4) + 160) and x < (50+(largura // 3)) and y < (((altura // 2) - (altura // 4) + 160) + placar):
                        sair = True
                        fimDeJogo = False
                        pos_x = randrange(0, largura - tamanho, 20)
                        pos_y = randrange(0, altura - tamanho - placar, 20)
                        maca_x = randrange(0, largura - tamanho, 20)
                        maca_y = randrange(0, altura - tamanho - placar, 20)
                        velocidade_x = 0
                        velocidade_y = 0
                        velocidade = 20
                        cobraXY = []
                        cobraComp = 3
                        pontos = 0
                    if x > (largura - (largura // 3) - 50) and y > ((altura // 2) - (altura // 4) + 160) and x < ((largura - (largura // 3) - 50) + (largura // 3)) and y < (((altura // 2) - (altura // 4) + 160) + placar):
                        sair = False
                        fimDeJogo = False

            fundo.fill(black)
            texto("GAME OVER", white, 50, largura // 2, (altura // 2) - (altura // 4), False)
            texto("Pontuação: "+str(pontos), white, 50, largura // 2, (altura // 2) - (altura // 4) + 80, False)

            pygame.draw.rect(fundo, green, [50, (altura // 2) - (altura // 4) + 160, largura // 3, placar])
            texto("Continuar(C)", black, 42, 60, (altura // 2) - (altura // 4) + 170, True)

            pygame.draw.rect(fundo, green, [largura - (largura // 3) - 50, (altura // 2) - (altura // 4) + 160, largura // 3, placar])
            texto("Sair(S)", black, 42, (largura - (largura // 3)+12), (altura // 2) - (altura // 4) + 170, True)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != velocidade:
                    velocidade_y = 0
                    velocidade_x = -velocidade
                if event.key == pygame.K_RIGHT and velocidade_x != -velocidade:
                    velocidade_y = 0
                    velocidade_x = velocidade
                if event.key == pygame.K_UP and velocidade_y != velocidade:
                    velocidade_x = 0
                    velocidade_y = -velocidade
                if event.key == pygame.K_DOWN and velocidade_y != -velocidade:
                    velocidade_x = 0
                    velocidade_y = velocidade

        fundo.fill(green)
        pos_x+=velocidade_x
        pos_y+=velocidade_y

        # Comer maça
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randrange(0, largura - tamanho, 20)
            maca_y = randrange(0, altura - tamanho - placar, 20)
            cobraComp += 1
            pontos += 1

        if sair:

            # Bordas
            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanho
            if pos_y + tamanho > altura - placar:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanho - placar

            cobraInicio = []
            cobraInicio.append(pos_x)
            cobraInicio.append((pos_y))
            cobraXY.append(cobraInicio)
            if len(cobraXY) > cobraComp:
                del cobraXY[0]
            if any(bloco == cobraInicio for bloco in cobraXY[:-3]):
                fimDeJogo = True

            #Placar
            pygame.draw.rect(fundo, black, [0, altura-placar, largura, placar])
            texto("Pontuação: "+str(pontos), white, 50, 20, altura-placar+10, True)

            cobra(cobraXY)
            maca(maca_x,maca_y)

            #Renderização
            pygame.display.update()
            relogio.tick(fps)
jogo()

pygame.quit()
