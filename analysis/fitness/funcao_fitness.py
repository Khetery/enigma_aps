from abc import ABC, abstractmethod

class funcao_fitness(ABC):
    epsilon = (3*10**-10,)

    @abstractmethod
    def pontuacao(self,texto):
        return 0.0
