numero_casos_teste = int(input("Digite o número de casos: "))
teste = 0

for teste in range(1, numero_casos_teste + 1):
    print("Teste {} de {}".format(teste, numero_casos_teste))
    escrever_painel = list(input("Digite o número que deverá aparecer no painel: "))

    numero_leds = 0

    for i in escrever_painel:
        if (i == "1"):
            numero_leds += 2
        elif (i == "2"):
            numero_leds += 5
        elif (i == "3"):
            numero_leds += 5
        elif (i == "4"):
            numero_leds += 4
        elif (i == "5"):
            numero_leds += 5
        elif (i == "6"):
            numero_leds += 6
        elif (i == "7"):
            numero_leds += 3
        elif (i == "8"):
            numero_leds += 7
        elif (i == "9"):
            numero_leds += 6
        elif (i == "0"):
            numero_leds += 6



    print(f"Serão necessários {numero_leds} leds!")

