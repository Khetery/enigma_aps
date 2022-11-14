class Rotor:
    _nome = ""
    _fiacaoDireta = []
    _fiacaoInversa =[]

    _posicaoRotor = 0
    _posicaoEntalhe = 0
    _configuracaoAnel = 0

    def __init__(self,nome,codificacao,posicaoRotor,posicaoEntalhe,configuracaoAnel):
        self._nome = nome
        self._fiacaoDireta = decodificaFiacao(codificacao)
        self._fiacaoInversa = fiacaoReversa(self._fiacaoDireta)
        self._posicaoRotor = posicaoRotor
        self._posicaoEntalhe = posicaoEntalhe
        self._configuracaoAnel = configuracaoAnel
    
    def Create(nome,posicaoRotor,configuracaoAnel):
        match nome:
            case "I":
                return Rotor("I","xyzwhibgdpfqjkeautnlcomrsv",posicaoRotor,16,configuracaoAnel)
            case "II":
                return Rotor("II","pjoxzcaqwtklhmvnfigsdbreyu",posicaoRotor,4,configuracaoAnel)
            case "III":
                return Rotor("III","pyqxmrsvteiozklawnhgjbcufd",posicaoRotor,21,configuracaoAnel)
            case "IV":
                return Rotor("IV","tkyubaeohsmvdqzxwpfrcngjli",posicaoRotor,25,configuracaoAnel)
            case "V":
                return Rotor("V","yipenwoftqrlzjabmcxvkhgsud",posicaoRotor,25,configuracaoAnel)
    
    def getNome(self):
        return self._nome
    
    def getPosicao(self):
        return self._posicaoRotor
    
    def decodificaFiacao(encoding):
        Fiacao = [len(encoding)]
        n=0
        for i in encoding:
            Fiacao[n]=ord(i)-97
        return Fiacao

    def fiacaoReversa(fiacao):
        inverso = [len(fiacao)]
        for i in range(len(fiacao)):
            
            

        