def fibonacci(num_elementos):
    lista = [0, 1, 1]
    if num_elementos == 1:
        return print(lista[0:2])
    elif num_elementos == 2:
        return print(lista)
    else:
        termo_aux1 = 1
        termo_aux2 = 1
        for elementos in range(2, num_elementos):
            termo_posi = termo_aux1 + termo_aux2
            termo_aux1 = termo_aux2
            termo_aux2 = termo_posi
            lista.append(termo_posi)
        return print(lista)


numero_elementos = 1
while (numero_elementos != 0):
    numero_elementos = int(
        input("Digite quantos elementos você deseja que tenha na sua sequência(0 para sair do programa): "))
    if numero_elementos == 0:
        print("Obrigado, até a próxima!")
    else:
        fibonacci(numero_elementos)
