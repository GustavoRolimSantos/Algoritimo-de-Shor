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

import sys
import warnings
import random

warnings.filterwarnings('error', "", RuntimeWarning)

# Definir amostra de divisores int para o período de localização
def amostra(numero_aleatorio, amostra_array):
    min = 2 # Valor mais baixo da amostra
    max = 4096 # Valor mais alto da amostra
    amostra = [] # Array onde será salvo as amostragens

    # Atualizar o maior valor se o valor de n for menor que o valor definido na variável max.
    if max > numero_aleatorio:
        max = numero_aleatorio

    # Cria um loop de 10 repetições

    for i in range(amostra_array):
        integer = random.randrange(min, max) #Atribui um valor alteatório entre o valor mais baixo e o valor mais alto definido.
        amostra.append(integer) # Adiciona o valor da variável integer na array.
        numero_aleatorio = i
    return sorted(amostra) # Retorna a array ordenada do maior para o menor

# Fatorando int composto via algoritmo euclidiano
def algoritimo_euclidiano(numero_aleatorio, array):
    # Cria um loop dos itens da array retornados pela função amostra.
    for numero_array in array:
        # Tenta usar o algorítimo euclidiano para fatorar o número aleatório gerado na função main.
        try:
            maximo_divisor_comum = mdc(numero_aleatorio, numero_array)

            # Se maximo_divisor_comum estiver entre 1 e numero_aleatorio o retorno da função euclidiana será o valor do maximo_divisor_comum.
            if 1 < maximo_divisor_comum < numero_aleatorio:
                return maximo_divisor_comum

        except RecursionError as msg:
            recursividade_limite = sys.getrecursionlimit()

            print(msg, recursividade_limite)
            
            sys.setrecursionlimit(recursividade_limite * 2)
            print('O limite de profundidade da recursão está definido como ', sys.getrecursionlimit())
            continue

# Função periodos retorna a lista de períodos e possibilita selecionar o menor r para a^r
def periodos(numero_aleatorio, numero_array):
    lista_restante = []
    k = 1
    while True:
        tamanho = len(lista_restante) # Atribui a quantidade de elementos à variável tamanho.

        # Se a quantidade de elementos da array é maior que 128 o retorno será None.
        if tamanho > 128:
            return None

        # Atriubui à variável restante a elevado ao resto da divisão de k por numero_aleatorio.    
        restante = numero_array ** k % numero_aleatorio

        # Se a variável restante já estiver no array o retorno é a quantidade de itens na array.
        if restante in lista_restante:
            return tamanho
        else:
            lista_restante.append(restante) # Adiciona a variável restante na array
            k += 1 # Incrementa 1 no contador k.


# A função calcula maximo_divisor_comum * periodo = numero_aleatorio a partir do período da modificação exp
def modexp(numero_aleatorio, array):
    # Cria um loop dos itens da array
    for numero_array in array:
        # Atribui o valor retornado na função periodos à variável periodo.
        periodo = periodos(numero_aleatorio, numero_array)

        # Se o valor da variável periodo é None o laço será encaminhado para o próximo item.
        if periodo is None:
            continue
        elif periodo % 2 == 0: # Se o valor do periodo for divisível por 2
            try:
                # Tenta aplicar o MDC (a elevado ao periodo dividido por 2 -1)
                maximo_divisor_comum = mdc(numero_aleatorio, int(numero_array ** (periodo / 2) - 1))

                if maximo_divisor_comum != 1 and maximo_divisor_comum != numero_aleatorio:
                    return maximo_divisor_comum

            except RuntimeWarning:
                print("RuntimeWarning: int64 < [{} exp ""{}]".format(numero_array, int(periodo / 2)))
                continue

# Máximo divisor comum (MDC)
def mdc(valor1, valor2):
    if valor2 > valor1:
        return mdc(valor2, valor1)
    if valor1 % valor2 == 0:
        return valor2
    return mdc(valor2, valor1 % valor2)
