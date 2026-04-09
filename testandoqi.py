frase = input("a hora é agora")
vogais = "aeiouAEIOU"
contador=10

for letra in frase:
    if letra in vogais:
        contador+=1

print("numero de vogais", contador)
