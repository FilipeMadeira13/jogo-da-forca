import os
import random

def carregar_palavras():
    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        return [linha.strip().upper() for linha in arquivo if linha.strip()]

palavras = carregar_palavras()

def iniciar_jogo():
    global palavra_secreta, erros, letras_certas
    palavra_secreta = random.choice(palavras).upper()
    erros = 0
    letras_certas = []

def exibir_nome_do_jogo():
    print('''
          
░░█ █▀█ █▀▀ █▀█   █▀▄ ▄▀█   █▀▀ █▀█ █▀█ █▀▀ ▄▀█
█▄█ █▄█ █▄█ █▄█   █▄▀ █▀█   █▀░ █▄█ █▀▄ █▄▄ █▀█
          ''')
    print()

def limpar_tela():
    os.system('cls')

def chutar_letra():
    letra = input('Escolha uma letra: ').strip().upper()

    if len(letra) != 1:
        print('Digite apenas uma letra.')
        voltar_ao_menu_principal()
    
    return letra

def voltar_ao_menu_principal():
    print()
    input('Digite uma tecla para voltar ')
    main()

def verificar_letra(letra):
    global erros
    if letra in palavra_secreta.upper():
        print(f'A letra {letra} está na palavra secreta.')
        letras_certas.append(letra)
    else:
        print(f'A letra {letra} não está na palavra secreta.')
        erros += 1
        if not perdeu():
            palavra_chance = 'chance' if erros == 5 else 'chances'
            print(f'Você ainda tem {6 - erros} {palavra_chance}.')

    for l in palavra_secreta.upper():
        if l in letras_certas:
            print(l, end='')
        else:
            print('_', end='')

    voltar_ao_menu_principal()

def venceu():
    return set(palavra_secreta.upper()) <= set(letras_certas)

def perdeu():
    return erros >= 6

def main():
    limpar_tela()
    exibir_nome_do_jogo()

    if perdeu():
        print('Você não tem mais chances.')
        print(f'A palavra secreta era {palavra_secreta}.')
        return

    if venceu():
        print('Parabéns! Você descobriu a palavra secreta.')
        return

    letra = chutar_letra()

    if letra:
        verificar_letra(letra)
        

if __name__ == '__main__':
    iniciar_jogo()
    main()