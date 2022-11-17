from enigma.Espelho import Espelho
from enigma.Plugboard import Plugboard
from enigma.Rotor import Rotor


class Enigma:

    rotorDireito = None
    rotorEsquerdo = None
    rotorMeio = None

    espelho = None
    plugboard = None

    def __init__(self, rotores,espelho , posicao_rotores, configuracaoAnel , plugboard_conections):
        self.rotorEsquerdo = Rotor.Create(rotores[0], posicao_rotores[0], configuracaoAnel[0])
        self.rotorMeio = Rotor.Create(rotores[1], posicao_rotores[1], configuracaoAnel[1])
        self.rotorDireito = Rotor.Create(rotores[2], posicao_rotores[2], configuracaoAnel[2])
        self.espelho = Espelho.criar(espelho)
        self.plugboard = Plugboard(plugboard_conections)

            

    def girar(self):
        #caso o rotor do meio tenha completado a volta
        if self.rotorMeio.eUmEntalhe():
            self.rotorMeio.darVolta()
            self.rotorEsquerdo.darVolta()
        #caso o rotor da direita tenha completado a volta
        elif self.rotorDireito.eUmEntalhe():
            self.rotorMeio.darVolta()

        self.rotorDireito.darVolta()
    
    def criptografa(self,c):
        self.girar()

        #entrada da plugboard
        c = self.plugboard.forward(c)

        #da direita pra esquerda
        c1 = self.rotorDireito.praFrente(c)
        c2 = self.rotorMeio.praFrente(c1)
        c3 = self.rotorEsquerdo.praFrente(c2)

        #espelho
        c4 = self.espelho.praFrente(c3)

        #reverso

        c5 = self.rotorEsquerdo.praTras(c4)
        c6 = self.rotorMeio.praTras(c5)
        c7 = self.rotorDireito.praTras(c6)

        #plugboard

        c7 = self.plugboard.forward(c7)

        return c7

    def encripta (self,input):
        input = input.upper()
        if len(input) == 1:
            return chr(self.criptografa(ord(input)-65)+65)
        else:
            output = [None]*len(input)
            for i,letter in enumerate(input):
                output[i] = chr(self.criptografa(ord(letter)-65)+65)
                print(self.rotorEsquerdo.getPosicao(),self.rotorMeio.getPosicao(),self.rotorDireito.getPosicao())
            return output

                



   



