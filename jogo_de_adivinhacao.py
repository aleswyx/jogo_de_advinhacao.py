# Este programa é um jogo de adivinhação. O usuário tenta adivinhar um número aleatório gerado pelo computador.

import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5
    
    print("Bem-vindo ao jogo de adivinhação! Você tem", max_tentativas, "tentativas para adivinhar o número secreto.")
    
    while tentativas < max_tentativas:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("O número secreto é maior que", palpite, ". Tente novamente!")
        elif palpite > numero_secreto:
            print("O número secreto é menor que", palpite, ". Tente novamente!")
        else:
            print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas!")
            return
    
    print("Você não conseguiu adivinhar o número secreto em", max_tentativas, "tentativas. O número secreto era", numero_secreto, ". Tente novamente!")
    
adivinhe_o_numero()
