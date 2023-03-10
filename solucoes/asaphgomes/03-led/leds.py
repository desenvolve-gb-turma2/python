n = int(input('Quantos casos de teste você pretende fazer? '))
algarismo = {'1' : 2,
  '2' : 5,
  '3' : 5,
  '4' : 4,
  '5' : 5,
  '6' : 6,
  '7' : 3,
  '8' : 7,
  '9' : 6,
  '0' : 6}

for i in range(n): 
  total_leds = input('Digite a formação de leds que você deseja montar: ')
  leds = 0
  for digito in total_leds: 
    if digito in algarismo:
        leds += algarismo[digito] # descobri que em dict dá pra usar a key como valor de index 
  print(leds, 'leds')
