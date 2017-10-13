***********************************************************
** CONTAR CADA ITEM OU CADA PALAVRA DE UM TEXTO OU LISTA **
***********************************************************


copas = ["Alemanha", "Espanha", "Italia", "Brasil", "França", "Brasil", "Alemanha", "Argentina", "Italia", "Argentina", "Alemanha", "Brasil", "Inglaterra", "Brasil", "Brasil", "Alemanha", "Uruguai", "Italia", "Italia", "Uruguai"]
campeoes = set(copas)

print()

for selecao in campeoes:
	num_vezes = copas.count(selecao)
	print(selecao + ":", num_vezes)
	
print()
print("Fim")

# VER conta_itens.sh
# VER conta_palavras.py
