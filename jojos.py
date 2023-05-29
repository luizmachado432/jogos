def jogar():
    import forca
    import adivinhacao

    print(28*"/")
    print("/   Escolha o seu jogo     /")
    print(28*"/","\n")

    while input == 0 or 4:

        print("(1) Adivinhação (2) Forca (3) Sair")
        jogo = (input("Qual jogo? "))
        
        if(jogo == str("1")):
            print ("Jogando Adivinhação")
            adivinhacao.jogar()
            return

        elif(jogo == str("2")):
            print ("Jogando Forca")
            forca.jogar()
            return

        elif(jogo == str("3")):
            print ("Saindo... ")
            break

        else:
            print(26*"*")
            print("*  Escolha entre 1 ou 2 // 3 = sair *")
            print(26*"*","\n")
            #print("Escolha entre 1 ou 2")

if(__name__ == '__main__'):
    jogar()