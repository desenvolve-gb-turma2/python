def fibonacci ():
  try:
    
    n = int(input('Quantos números terá a sequencia fibonacci? '))
    fibonacci = [0,1]
    
    if n < 0:
      return 'Digite um número inteiro positivo!'
    elif n == 0:
      return []
    elif n == 1:
      return [0]
    elif n >= 2:
      for i in range (n-2):
        fibonacci.append((fibonacci [-1]) + (fibonacci [-2]))
    return fibonacci
    
  except ValueError: 
    return 'Digite um número inteiro positivo!'
    
print(fibonacci())
