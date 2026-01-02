#Calcular a hipotenusa
from math import hypot

x = float (input("Digite o cateto oposto: "))
y = float (input("Digite o cateto adjacente: "))

# print (f"A hipotenusa e {sqrt(x*x + y*y):.2f}")
print (f"A hipotenusa mede {hypot(x,y):.2f}")