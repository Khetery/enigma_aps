from enigma.Enigma import Enigma

rotor1 = input("Qual é o primeiro rotor?(I-V)")
rotor2 = input("Qual é o segundo rotor?(I-V)")
rotor3 = input("Qual é o terceiro rotor?(I-V)")
espelho = input("O modelo do refletor é B ou C?")

pos1 = int(input("Qual a posição inicial do primeiro rotor?(0-25)"))
pos2 = int(input("Qual a posição inicial do segundo rotor?(0-25)"))
pos3 = int(input("Qual a posição inicial do terceiro rotor?(0-25)"))

anel1 = int(input("Qual deve ser a variação do output para o rotor1?(0-25)"))
anel2 = int(input("Qual deve ser a variação do output para o rotor2?(0-25)"))
anel3 = int(input("Qual deve ser a variação do output para o rotor3?(0-25)"))

maquinaenigma = Enigma([rotor1,rotor2,rotor3],espelho,[pos1,pos2,pos3],[anel1,anel2,anel3],None)

aserencriptado = input("máquina configurada, qual texto devemos transformar?")

texto = maquinaenigma.encripta(aserencriptado)

print("O texto resultante é :")
print("".join(texto))
