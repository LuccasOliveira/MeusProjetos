# random utilizada na classe Simulador
import random

# CONSTANTES
CAP_MIN = 10
CAP_MAX = 51 # Capacidade maxima, ja ajustada com +1 para randrange
VOL_MIN = 1
VOL_MAX = 11 # volume sorteado maximo, ja ajustado com +1

# ----------------------------------------------------------------------------

def main():
    ''' Controla a entrada e saida.
    '''
    #leitura da semente para criar o simulador
    semente = int(input("Digite a semente do gerador aleatorio: "))
    jogo    = Simulador(semente)
    continua= True
    cheio   = False

    print("\nInicio da simulacao")
    while not cheio and continua:
        # sorteia o proximo valor
        jogo.sorteia()
        opcao = input("Deseja adicionar? (s/n) : ")
        if opcao == 's':
            cheio = jogo.deposita()
        else:
            continua = False
    jogo.finaliza()

# ----------------------------------------------------------------------------

class Balde:
    '''
        A classe Balde modela um recipente com capacidade (cap) e
        volume atual (vol).

        Ela armazena tambem o volume derramado e indica se esta cheio.
    '''
    def __init__(self, c):
        self.cap = c
        self.vol = 0  # volume atual
        self.der = 0  # volume derramado
        self.cheio = False

    def deposita(self, v):
        '''
            Deposita um volume de agua (v) e atualiza o estado do Balde.
        '''
        self.vol += v
        if self.vol >= self.cap:
            self.cheio = True
            self.der = self.vol - self.cap
            self.vol = self.cap

    def __repr__(self):
        if self.vol == self.cap:
            return "*%2d*"%self.vol
        else:
            return "[%2d]"%self.vol

# ----------------------------------------------------------------------------

class Simulador:
    ''' classe Simulador mantem o estado da simulacao e
        os procedimentos para simular. Note que a classe
        Simulador "esconde" o modulo random da funcao main.
    '''
    def __init__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAP_MIN, CAP_MAX)
        self.rec = Balde(capacidade)
        self.vol = 0
        self.avisou = False

    def sorteia(self):
        self.vol = random.randrange(VOL_MIN, VOL_MAX)
        print()
        print("Volume atual   : ", self.rec.vol)
        print("Volume sorteado: ", self.vol)

    def deposita(self):
        ''' adiciona o ultimo volume sorteado self.vol
            ao balde e retorna True se o
            balde estiver cheio e False caso contrario.
            '''
        self.rec.deposita( self.vol )

        if self.rec.vol >= self.rec.cap/2 and not self.avisou:
            self.avisou = True
            print("O volume do balde atingiu/passou a metade.")

        return self.rec.cheio

    def finaliza(self):
        print("\nFim da simulacao")
        print("Capacidade do balde: %d" % self.rec.cap)
        print("Volume final: %d" % self.rec.vol)

        if self.rec.der > 0:
            print("Balde esta cheio e houve derramamento de agua")
            print("Volume derramado foi: %d" %(self.rec.der))
        else:
            if self.rec.cheio:
                print("Balde esta cheio e nao houve derramamento de agua")
            elif self.rec.cap - self.rec.vol >= self.vol:
                print("Balde nao esta cheio.")
                print("Havia espaco para o ultimo volume sorteado: %d" % self.vol)
            else:
                print("Balde nao esta cheio.")
                print("Nao havia espaco para o ultimo volume sorteado: %d" % self.vol)


# ----------------------------------------------------------------------------

main()
