import funcao_fitness

class fitnessioc (funcao_fitness.funcao_fitness):
    
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Essa função define se a entrada é uma letra
    def e_letra (self,entrada):
        return (entrada in self.alfabeto) 

    #Essa função conta a quantidade de letras no texto
    def conta_letras (self,texto):
        conta = 0
        for letra in texto:
            if self.e_letra (letra):     
                conta+=1
        return conta

    def pontuacao (self,texto):    
        contagem_de_letras = [] 

        #Esse pedaço é responsável por contar quantas vezes cada letra aparece
        for i in range(0,25):
            conta = 0 
            for j in texto:
                if j == self.alfabeto[i] or j == self.alfabeto[i+26]:
                    conta +=1
            contagem_de_letras.append(conta)
        
        #Esse pedaço percorre todas as contagens de letra e aplica a formula
        total = 0 
        for i in range(0,25):
            vezes_letra_apareceu = contagem_de_letras[i]
            total += vezes_letra_apareceu * (vezes_letra_apareceu-1)

        numero_letra_texto = self.conta_letras(texto)
        total = float(total) / (numero_letra_texto*(numero_letra_texto-1))
        return total



