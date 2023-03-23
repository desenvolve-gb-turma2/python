def fibonacci():

    elementos = int(input("Digite a quantidade de elementos a calcular: "))

    t1 = 1
    t2 = 1
    count = 0

    lista = [1,1]
    if elementos > 0:
        if elementos == 1:
            print("1")
        elif elementos == 2:
            print(lista)
        else:
            for count in range(2, elementos):
                count = t1 + t2
                t1 = count
                t2 = (count - t2)
                lista.append(count)

            print(lista)
    else:
        print(f"O valor {elementos} não é um número válido!")
        print(f"Insira um número inteiro positivo e tente novamente!")


if(__name__ == "__main__"):
    fibonacci()