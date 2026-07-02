import os
import random

VERDE = '\033[92m'
VERMELHO = '\033[91m'
RESET = '\033[0m'

def carregar_palavras():
    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        return [linha.strip().upper() for linha in arquivo if linha.strip()]

palavras = carregar_palavras()

def reiniciar_opcoes_jogo():
    global palavra_secreta, erros, letras_certas, letras_escolhidas
    palavra_secreta = random.choice(palavras).upper()
    erros = 0
    letras_certas = []
    letras_escolhidas = []

def iniciar_jogo():
    reiniciar_opcoes_jogo()
    menu_iniciar()

def mostrar_opcoes():
    print('1. Jogar')
    print('2. Ver regras')
    print('3. Sair')

def escolher_opcao_inicio_jogo():
    try:
        opcao = int(input('Escolha o número da opção: ').strip())

        if opcao == 1:
            main()
        elif opcao == 2:
            limpar_tela()
            with open('regras.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    if linha.strip():
                        print(linha.strip())
            
            input()
            menu_iniciar()

        elif opcao == 3:
            limpar_tela()
            print('Você saiu do jogo.')
            return
        
    except ValueError as e:
        print(f'Erro: {e}')

def menu_iniciar():
    limpar_tela()
    exibir_nome_do_jogo()
    mostrar_opcoes()
    escolher_opcao_inicio_jogo()

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
        return None
    
    if not letra.isalpha():
        print('Digite apenas letras (sem números ou símbolos).')
        voltar_ao_menu_principal()
        return None
    
    return letra

def voltar_ao_menu_principal():
    print()
    input('Digite uma tecla para voltar ')
    main()

def verificar_letra(letra):
    global erros
    letra = letra.upper()

    if letra in letras_escolhidas:
        print(f'A letra {letra} já foi escolhida.')
        voltar_ao_menu_principal()
        return

    letras_escolhidas.append(letra)

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

def reiniciar_partida():
    reiniciar = input('Deseja reiniciar a partida? (S/N): ').lower().strip() == 's'

    if reiniciar:
        iniciar_jogo()

def mostrar_palavra_final(vitoria):
    cor = VERDE if vitoria else VERMELHO
    palavra_formatada = ' '.join(palavra_secreta.upper())
    largura = len(palavra_formatada) + 4

    print()
    if vitoria:
        print('🎉 ' + '═' * largura + ' 🎉')
        print(f'   PARABÉNS, VOCÊ VENCEU!')
    else:
        print('💀 ' + '═' * largura + ' 💀')
        print(f'   FIM DE JOGO...')

    print(f'{cor}[ {palavra_formatada} ]{RESET}')
    print('═' * (largura + 4))
    print()

def main():
    limpar_tela()

    if perdeu():
        mostrar_palavra_final(vitoria=False)
        reiniciar_partida()
        return

    if venceu():
        mostrar_palavra_final(vitoria=True)
        reiniciar_partida()
        return

    letra = chutar_letra()

    if letra:
        verificar_letra(letra)
        

if __name__ == '__main__':
    iniciar_jogo()