import chave_enigma

class pontuacao_enigma(chave_enigma):
    pontuacao = 0.0

    def __init__(self, chave_enigma, pontuacao):
        super().__init__(chave_enigma)
        self.pontuacao = pontuacao

    def get_pontuacao (self):
        return self.pontuacao

    def compare_com (self, pontuacao_enigma):
        if self.pontuacao < pontuacao_enigma.pontuacao:
            return -1
        elif self.pontuacao == pontuacao_enigma.pontuacao:
            return 0
        else:
            return 1 