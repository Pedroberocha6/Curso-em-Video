# Ler um angulo e mostra seu seno, cosseno e tangente
import math

num = float (input ("Digite o valor do angulo: "))
numRadi = math.radians(num)
print (f"O cosseno de {num} e {math.cos(numRadi):.2f}, o seno e {math.sin(numRadi):.2} e a tangente e {math.tan(numRadi):.2}")