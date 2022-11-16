from analysis import chave_enigma 
import Espelho,Plugboard,Rotor


class enigma:

    rotorDireito = ""
    rotorEsquerdo = ""
    rotorMeio = ""

    espelho = ""
    plugboard = ""

    def __init__(self, rotores, posicao_rotores, configuracaoAnel, espelho, plugboard_conections):
       if not isinstance(rotores, chave_enigma):
            self.rotorEsquerdo = Rotor(rotores[0], posicao_rotores[0], configuracaoAnel[0])
            self.rotorMeio = Rotor(rotores[1], posicao_rotores[1], configuracaoAnel[1])
            self.rotorDireito = Rotor(rotores[2], posicao_rotores[2], configuracaoAnel[2])
            self.espelho = Espelho(espelho)
            self.plugboard = Plugboard(plugboard_conections)
        else:
            
        this(rotores.rotors, "B", rotores.indicators, rotores.rings, rotores.plugboard)
            self.rotorEsquerdo = Rotor(rotores.rotores[0], "0", configuracaoAnel[0])
            self.rotorMeio = Rotor(rotores.rotores[1], "0", configuracaoAnel[1])
            self.rotorDireito = Rotor(rotores.rotores[2],"0" , configuracaoAnel[2])
            self.espelho = Espelho(espelho)
            self.plugboard = Plugboard(plugboard_conections)
            



   



