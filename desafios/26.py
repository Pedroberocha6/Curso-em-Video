frase = input ("Digite sua frase: ").strip()
fraseUpper = frase.upper()

print (f"A letra A aparece {fraseUpper.count('A')} vezes.")
print (f"A letra A aparece a primeira vez na posicao {fraseUpper.find("A")+1}.")
print (f"A ultima aparece na posicao {fraseUpper.rfind("A")+1}")