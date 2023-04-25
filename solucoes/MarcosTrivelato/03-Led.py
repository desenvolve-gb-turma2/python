# Esta versão usa match e case, que só está presente a partir do Python 3.10
# Há maneiras mais eficientes de fazer este código, como criar uma lista, com os valores de cada caso, mas quis praticar um pouco a estrutura case
def numero_de_leds(numero):
    match numero:
        case "1":
            return 2

        case "2":
            return 5

        case "3":
            return 5

        case "4":
            return 4

        case "5":
            return 5

        case "6":
            return 6

        case "7":
            return 3

        case "8":
            return 7

        case "9":
            return 6

        case "0":
            return 6

#função que conta o numero de leds utilizado
def conta_leds(numero):
    total_leds = 0
    for x in numero:
        total_leds += numero_de_leds(x)
    return total_leds

#recebendo o número de linhas de input
linhas = int(input())
numeros = []

#recebendo os números a serem construido com leds
for i in range(linhas):
    numeros.append(input())

#resultado
for numero in numeros:
    total_leds = conta_leds(numero)
    print(f'{total_leds} leds')
