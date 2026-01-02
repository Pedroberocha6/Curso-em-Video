from random import sample

alunos = ["Pedro", "Julia", "Lucas", "Fernanda"]
ordem = sample(alunos, k = 4)
textoFinal = ",".join(ordem)

print (f"A ordem de apresentacao sera {textoFinal} ")