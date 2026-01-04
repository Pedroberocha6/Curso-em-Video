frase = "Curso em video Python"
print (frase[3])
print (frase[3:13]) 
print (frase[:13])
print (frase [2:15:2])
print (frase [::2])

print ("""Texto é uma produção, verbal ou não verbal, que se constitui com algum
código, no intuito de comunicar algo a alguém, em determinado tempo e  espaço. 
Sua definição ampla se deve ao fato de também abranger diversos formatos"""  ) # Usar 3 aspas para grandes textos

print (frase.count("o"))
print (frase.upper().count("O"))
print (len(frase))
print (frase.replace("Python", "Android"))
print (frase)
frase = frase.replace("Python", "Android")
print (frase)
print ("Curso" in frase)
print (frase.find("Curso"))

print (frase.split()) #Transforma em lista
dividido = frase.split()
print (dividido[0] [3])