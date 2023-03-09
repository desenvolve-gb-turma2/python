def fibonacci ():
  n = int(input('Quantos números terá a sequencia fibonacci? '))
  fibonacci = [0,1]

  for i in range (n-2):
    fibonacci.append((fibonacci [-1]) + (fibonacci [-2]))
  
  return fibonacci
  #return ", ".join(str(numero) for numero in fibonacci)

print(fibonacci())
