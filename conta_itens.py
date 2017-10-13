***********************************************************
** CONTAR CADA ITEM OU CADA PALAVRA DE UM TEXTO OU LISTA **
***********************************************************


copas = ["Alemanha", "Espanha", "Italia", "Brasil", "França", "Brasil", "Alemanha", "Argentina", "Italia", "Argentina", "Alemanha", "Brasil", "Inglaterra", "Brasil", "Brasil", "Alemanha", "Uruguai", "Italia", "Italia", "Uruguai"]
campeoes = set(copas)

qtas_copas = copas.len()
qtos_campeoes = campeoes.len()

print()
print("Em toda história, tivemos", qtas_copas, "Copas do Mundo...")
print("com", qtos_campeoes, "seleções campeãs!")
print()

for selecao in campeoes:
	num_vezes = copas.count(selecao)
	print(selecao + ":", num_vezes)
	
print()
print("Fim")

# VER conta_itens.sh
# VER conta_palavras.py
