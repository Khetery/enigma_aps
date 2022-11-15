class Plugboard:
    __fiacao = []

    def __init__(self,conexoes):
        self.__fiacao = self.decodificaPlugboard(conexoes)
    
    def praFrente(self,c):
        return self.__fiacao[c]

    @staticmethod
    def identidadePlugboard():
        mapeamento = [26]
        for i in range(26):
            mapeamento[i] = i
        return mapeamento
    
    @staticmethod
    def getCaracteresDesplugados(plugboard):
        caracteresDesplugados = {}
        for i in range(26):
            caracteresDesplugados.add(i)
        
        if plugboard == "" :
            return caracteresDesplugados
        
        pares = plugboard.split("[^a-zA-Z]")

        for par in pares:
            
    

    
