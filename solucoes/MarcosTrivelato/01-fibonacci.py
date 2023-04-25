def fibonacci(e: int):
    if e<2:
        print("Este número não é apropriado para criar a sequencia, por favor entre um número >=2")
    
    lista_fibonacci = []
    for i in range(e):
        if i < 2:
            lista_fibonacci.append(i)
        else:
            a = lista_fibonacci[i - 1] + lista_fibonacci[i - 2]
            lista_fibonacci.append(a)

    return lista_fibonacci