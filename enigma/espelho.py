class Espelho:

    _fiacaoDireta = []

    def __init__(self, codificacao):
        self._fiacaoDireta = self._decodificaFiacao (codificacao)
        
    @staticmethod
    def criar(nome):
        match nome:
            case "B": 
                return Espelho("YRUHQSLDPXNGOKMIEBFZCWVJAT")
            case "C":
                return Espelho("FVPJIAOYEDRZXWGCTKUQSBNMHL")
            case other:
                return Espelho("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    
    @staticmethod 
    def _decodificaFiacao(codificacao):
        charfiacao = codificacao
        fiacao = [len(charfiacao)]
        for i in range(0,len(charfiacao,1)):
            fiacao[i] = ord(charfiacao[i])-65
        return fiacao
    
    def praFrente(self,c):
        return self._fiacaoDireta[c]

        
