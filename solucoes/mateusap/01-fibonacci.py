def fibonacci (e: int):
    sequencia = []
    
    if e == 0 or e == 1:
        return "1" #coloquei o número 1 pra não retornar a lista vazia
    elif e <= 0:
        return "Fibonacci não trabalha com números negativos"
    
    sequencia = [1,1] #valores iniciais da sequencia seguindo o exemplo usando 1 e 1 ao invés de 0 e 1
    atual = 1
    anterior = 1

    for i in range (2, e):
        proximo = atual + anterior
        sequencia.append(proximo)
        anterior = atual
        atual = proximo

    return sequencia

#seq = fibonacci(7) teste da função pra ver se estava funcionando
#print (seq)
