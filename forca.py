def jogar():
    import random

    from os import environ
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import pygame


    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    arquivo = open("palavras.txt" , "r")
    palavras = []

    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()
#tirar o comentario aqui#################################
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras [numero].upper()

    print(palavra_secreta)
#########################################################
    enforcou = False
    acertou = False
    erros = 0

    #palavra_secreta = "a".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    while(not enforcou and not acertou):
            
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    #print("Encontrei a letra {} na posição {}" .format(letra, index))
                    letras_acertadas[index] = letra
                    som_acertou = pygame.mixer.Sound('som_acertou.wav')
                    som_acertou.play()
                #acertou_som()
                index += 1
        elif(chute != palavra_secreta):
            erros += 1
            errou_som = pygame.mixer.Sound('som_errou.wav')
            errou_som.play()
            #pygame.mixer.music.play()
            #errou_som()
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou, joga mt krl")
        imprime_mensagem_vencedor()
        venceu_som = pygame.mixer.Sound('som_win.wav')
        venceu_som.play()
    else:
        print("Você perdeu, a palavra era",(palavra_secreta))
        foi_destruido_ta_morto_seu_horroroso()
"""         perdeu_som = pygame.mixer.Sound('som_lose.wav')
        perdeu_som.play() """

"""         else:
            if(acertou):
                print("Você ganhou, joga mt krl")
                imprime_mensagem_vencedor()
                venceu_som = pygame.mixer.Sound('som_win.wav')
                venceu_som.play()
                #pygame.mixer.music.play()

            elif(enforcou):
                print("Você perdeu, a palavra era",(palavra_secreta))
                foi_destruido_ta_morto_seu_horroroso()
                #print(palavra_secreta) """



        



    #print(letras_acertadas)

    #print("Fim do jogo")

def foi_destruido_ta_morto_seu_horroroso():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    import pygame
    perdeu_som = pygame.mixer.Sound('som_lose.wav')
    perdeu_som.play()
    import jojos
    jojos.jogar() 
    return False

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    import jojos
    jojos.jogar() 
    return False

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


""" import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
pygame.init()
pygame.font.init()
pygame.mixer.init()
    #pygame.mixer.music.set_volume(0.2)
acertou_som = pygame.mixer.music.load('som_acertou.wav')

errou_som = pygame.mixer.music.load('som_errou.wav')

venceu_som = pygame.mixer.music.load('som_win.wav') """


if(__name__ == '__main__'):
    jogar()