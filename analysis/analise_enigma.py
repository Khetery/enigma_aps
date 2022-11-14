from analysis.fitness.ioc import faz_ioc

class analise_enigma:

    def acha_configuracao_rotor (texto_cifrado, chave_necessaria, plugboard, funcao_fitness):
        rotores_disponiveis = ["I","II","III","IV","V"]

        rotores_otimizados = []
        posicoes_otimizadas = []

        conjunto_de_chaves = []
        
        for rotor1 in rotores_disponiveis:
            for rotor2 in rotores_disponiveis:
                if rotor1 == rotor2: continue 
                for rotor3 in rotores_disponiveis:
                    if rotor1 == rotor3 or rotor2 == rotor3: continue
                    print(rotor1,"",rotor2,"",rotor3)

                    maximo_fitness = 10**(-30)
                    chave_enigma = None
                    for i in range(0,26,1):
                        for j in range(0,26,1):
                            for k in range(0,26,1):
                                e = Enigma([rotor1,rotor2,rotor3],"B",[i,j,k], [0,0,0], plugboard) #importar quando estiver pronto
                                decriptar = (texto_cifrado)
                                



                
 
