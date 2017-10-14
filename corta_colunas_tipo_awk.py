planetas=["Marte", "Jupiter", "Mercurio", "Venus", "Saturno"]

for planeta in planetas:
	
	arqFonte=planeta+".csv"			# Concatena variavel para formar nome do arquivo
	arqGerado=planeta+".txt"

#	arqFonte='Marte.csv'
#	arqSaida=open('marte.txt', 'a')

	arqSaida=open(arqGerado, 'a')
		
	with open(arqFonte, 'r') as arquivo:
		for linha in arquivo:
			corte1=linha.split(';')[0]	# Pega primeira coluna
			corte2=corte1.split(' ')[0]	# Faz outro corte do que já cortei acima
			corteA=linha.split(';')[1]	# Pega segunda coluna
			corteB=corteA.split("'")[3]	# Faz outro corte na linha acima - Ver *OBS

			print(corte2, corteB)		# Imprime na tela ao mesmo tempo que grava em arquivo. Ver abaixo:
			arqSaida.write(corte2 + '-' + corteB + '\n')

	arqSaida.close()				# Fecha arquivo de escrita (de saida)
	#arqFonte.close() - Nao precisa fechar arq aberto para leitura!!! Dá erro.


"""

(*) OBS - Este é o modelo de cada linha do arqFonte:

2017/10/12 00:00:00;('Vir', 'Virgo');13:53:23.08;-10:32:04.1;13:54:17.90;-10:37:02.8

"""
