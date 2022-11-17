from enigma.Enigma import Enigma

maquinaenigma = Enigma(["I","IV","V"],"C",[8,6,13],[1,3,5],None )

texto = maquinaenigma.encripta("")

print(string(texto))