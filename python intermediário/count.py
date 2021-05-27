from itertools import count

# comeca de 23 e pula de 2 em 2
contador = count(start=23, step=2)

for value in contador:
    print(value)

    if(value > 100):
        break