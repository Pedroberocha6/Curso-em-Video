nome = input ("Digite seu nome completo: ").strip()
dividido = nome.split()

print (f"Seu primeiro nome e {dividido[0]}")
print (f"Seu ultimo nome e {dividido[-1]}")