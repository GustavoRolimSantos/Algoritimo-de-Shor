'''

 PROJETO ALGORÍTIMO QUÂNTICOS [SHOR]
 FATEC AMERICANA - 2º SEMESTRE
 DISCIPLINA: CÁLCULO I

 © 2019, DIREITOS RESERVADOS À:
  - GUSTAVO ROLIM DOS SANTOS
  - MAICON GABRIEL DE SÁ
  - ANDRÉ NICOLA
  - VINÍCUS TENOMARO


'''

import random
import sys
import Processamento

# Variáveis Globais
indice = 3
limite = 10 ** indice  # Limite do número inteiro a ser fatorado
amostra = 10  # Número de inteiros em uma amostra para encontrar um período
tentativas = 3 # Número de tentativas para resolução da fatoração

def executar():
    # Define valor aleatório para n entre 100 10000
    numero_aleatorio = random.randint(10 ** (indice - 1), limite)

    # Atribui a array retornada pela função sample à variável numeros_lista
    numeros_lista = Processamento.amostra(numero_aleatorio, amostra)

    # Atribui à variável p o valor retornado pela função euclidiana (número aleatório e array).
    valor_euclidiano = Processamento.algoritimo_euclidiano(numero_aleatorio, numeros_lista)
    
    try:
        # Tenta usar o Algorítimo Euclidiano
        # Se o p não for None atribui à variável divisao a divisão de n por valor_euclidiano
        if valor_euclidiano is not None:
            divisao = int(numero_aleatorio / valor_euclidiano)
        else:
            # Caso o Algorítimo Euclidiano falhe tentará usar o modexp.
            print("\n[ALGORÍTIMO DE SHOR] Falha no algoritmo euclidiano.")
            valor_euclidiano = Processamento.modexp(numero_aleatorio, numeros_lista)

            # Se o p não for None atribui à variável divisao a divisão de numero_aleatorio por valor_euclidiano
            if valor_euclidiano is not None:
                divisao = int(numero_aleatorio / valor_euclidiano)
            else:
                valor_euclidiano, divisao = 1, numero_aleatorio
                print("[ALGORÍTIMO DE SHOR] Falha no algoritmo Modexp clássico.\n")

    except OverflowError as msg:
        divisao = 'divisao'
        print('Não foi possível encontrar o segundo fator divisao = numero_aleatorio / valor_euclidiano, causa: ', msg)

        if valor_euclidiano is None:
            valor_euclidiano = 'problema'

    print("OPERAÇÃO: {} x {} = {}".format(valor_euclidiano, divisao, numero_aleatorio))


def main():
    sys.setrecursionlimit(1000)

    print("---------------------------------------\n")
    print(" ALGORÍTIMO DE SHOR")
    print(" FATEC AMERICANA - 2º SEMESTRE")
    print(" DISCIPLINA: CÁLCULO I\n")
    print(" PROJETO DESENVOLVIDO POR:")
    print(" </> André Nicola")
    print(" </> Gustavo Rolim dos Santos")
    print(" </> Maicon Gabriel de Sá")
    print(" </> Vinícius Tenomaro")
    print("\n---------------------------------------")

    print("\nDigite o número de tentativas para resolução da fatoração: ")
    tentativas = input()
    
    while True:
        try:
            tentativas = int(tentativas)
            break
        except:
            print("[ALGORÍTIMO DE SHOR] As tentativas devem ser um número!")
            tentativas = input()

    print("")

    for _ in range(tentativas):
        executar()

if __name__ == '__main__':
    main()
    
