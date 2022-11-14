class chave_enigma:
    rotores = []
    indicadores = []
    posicao_inicial_rotores = []
    plugboard = ""

    def __init__(self, coringa, indicadores = None, posicao_inicial_rotores = None, plugboard_conections = None):
        if isinstance(coringa, chave_enigma): 
            self.rotores = coringa.rotores if coringa.rotores != None else ["I","II","III"]
            self.indicadores = coringa.indicadores if coringa.indicadores != None else [0,0,0]
            self.posicao_inicial_rotores = coringa.posicao_inicial_rotores if coringa.posicao_inicial_rotores != None else [0,0,0]
            self.plugboard = coringa.plugboard if coringa.plugboard != None else ""
    
        elif isinstance(coringa, list):
            self.rotores = coringa if coringa != None else ["I","II","III"]
            self.indicadores = indicadores if indicadores != None else [0,0,0]
            self.posicao_inicial_rotores = posicao_inicial_rotores if posicao_inicial_rotores != None else [0,0,0]
            self.plugboard = plugboard_conections if plugboard_conections != None else ""
            