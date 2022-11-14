alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Essa função define se a entrada é uma letra
def e_letra (entrada):
    return (entrada in alfabeto) 

#Essa função conta a quantidade de letras no texto
def conta_letras (texto):
    conta = 0
    for letra in texto:
        if e_letra (letra):     
            conta+=1
    return conta

def faz_ioc (texto):    
    contagem_de_letras = [] 

    #Esse pedaço é responsável por contar quantas vezes cada letra aparece
    for i in range(0,25):
        conta = 0 
        for j in texto:
            if j == alfabeto[i] or j == alfabeto[i+26]:
                conta +=1
        contagem_de_letras.append(conta)
    
    #Esse pedaço percorre todas as contagens de letra e aplica a formula
    total = 0 
    for i in range(0,25):
        vezes_letra_apareceu = contagem_de_letras[i]
        total += vezes_letra_apareceu * (vezes_letra_apareceu-1)

    numero_letra_texto = conta_letras(texto)
    total = float(total) / (numero_letra_texto*(numero_letra_texto-1))
    return total

texto = input("Digite um Texto:")
total = faz_ioc(texto)
print("IOC:" + str(total*26.0))

