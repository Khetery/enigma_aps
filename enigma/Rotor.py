class Rotor:
    _nome = ""
    _fiacaoDireta = []
    _fiacaoInversa =[]

    _posicaoRotor = 0
    _posicaoEntalhe = 0
    _configuracaoAnel = 0

    

    def getNome(self):
        return self._nome
    
    def getPosicao(self):
        return self._posicaoRotor
    
    def decodificaFiacao(self,encoding):
        Fiacao = [None]*len(encoding)
        for i,letter in enumerate(encoding):
            Fiacao[i]=ord(letter)-97
        return Fiacao

    def fiacaoReversa(self,fiacao):
        inverso = [None]*len(fiacao)
        for i in range(len(fiacao)):
            praFrente = fiacao[i]
            inverso[praFrente] = i
        return inverso

    def encifra(self,k,pos,anel,mapeamento):
        shift = pos - anel
        return (mapeamento[(k+shift+26)%26] -shift+26)%26
    
    def praFrente(self,c):
        return self.encifra(c,self._posicaoRotor,self._configuracaoAnel,self._fiacaoDireta)
    
    def praTras(self,c):
        return self.encifra(c,self._posicaoRotor,self._configuracaoAnel,self._fiacaoInversa)

    def eUmEntalhe(self):
        return self._posicaoRotor == self._posicaoEntalhe

    def darVolta(self):
        self._posicaoRotor = (self._posicaoRotor+1)%26
    

    def __init__(self,nome,codificacao,posicaoRotor,posicaoEntalhe,configuracaoAnel):
        self._nome = nome
        self._fiacaoDireta = self.decodificaFiacao(codificacao)
        self._fiacaoInversa = self.fiacaoReversa(self._fiacaoDireta)
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
    
            

        