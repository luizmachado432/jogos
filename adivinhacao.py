#print("bah", "meo", sep="\n")
def jogar():
    import random
    import jojos

    print(29*"/")
    print("/   O Jogo da Adivinhação   / ")
    print(29*"/","\n")

    #numero_secreto = 5
    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    #pontos = 1000
    rodada = 1
    #print(numero_secreto)
    acertou = False

    while input == 0 or 4:
        print("Escolha a dificuldade")
        print("(1) Facil (2) Médio (3) Difícil // (4) Voltar")
        nivel = int(input("Digite o nível de dificuldade escolhido: "))
        if(nivel == 1):
            total_de_tentativas = 20

        elif(nivel == 2):
            total_de_tentativas = 10

        elif(nivel == 3):
            total_de_tentativas = 1
        
        elif(nivel == 4):
            jojos.jogar()
            break

        else:
            (nivel <= 0 or nivel >= 4)
            print(29*"*")
            print("*  Escolha entre 1, 2 ou 3  *")
            print(29*"*","\n")


        while (rodada <= total_de_tentativas):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute_str = input("Digite o seu número: ")
            print("Você digitou " , chute_str)
            chute = int(chute_str)
            if (chute < 1 or chute > 100):
                print("Só é valido números de 1 a 100")
                continue

            acertou = chute == numero_secreto

            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print("Parabéns! Você acertou!")
                jojos.jogar()
                break

            #if int(rodada == rodada +1):
                        #print("o numero secreto era:", (numero_secreto))

            else:
                if(maior):
                    print("O seu chute foi maior do que o número secreto!")
                elif(menor):
                    print("O seu chute foi menor do que o número secreto!")
                    #print("O número era", (numero_secreto))
            rodada = rodada +1

    #Mostrar os pontos quando finaliza

        if nivel == 1 and rodada == 21 and acertou == False:
                print("O numero secreto era:", (numero_secreto))
                print("Fim do jogo")
                jojos.jogar()

        if nivel == 2 and rodada == 11 and acertou == False:
                print("O numero secreto era:", (numero_secreto))
                print("Fim do jogo")
                jojos.jogar()

        if nivel == 3 and rodada == 2 and acertou == False:
                print("O numero secreto era:", (numero_secreto))
                print("Fim do jogo")
                jojos.jogar()

                #print("Fim do jogo")
                #jojos.jogar()

if(__name__ == '__main__'):
    jogar()