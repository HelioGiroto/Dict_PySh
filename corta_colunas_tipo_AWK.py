#############################################################
## Como cortamos CAMPOS de arq CSV tal como se faz no AWK  ##
#############################################################

planetas=["Marte", "Jupiter", "Mercurio", "Venus", "Saturno"]	# Essa lista é na vdd nomes de arquivos

for planeta in planetas:
	
	arqCSV = planeta+".csv"				# Concatena variável para formar nome dos arquivos
	arqTXT = planeta+".txt"

	arqFonte = open(arqCSV, 'r')
	arqSaida = open(arqTXT, 'a')

	for cada_linha in arqFonte:
		corte1 = cada_linha.split(';')[0]	# Corta primeira coluna
		corte2 = corte1.split(' ')[0]		# Faz outro corte naq. que já cortei acima
		
		corteA = cada_linha.split(';')[1]	# Corta segunda coluna
		corteB = corteA.split("'")[3]		# Faz outro corte na linha acima - (Ver *OBS - rodapé)

		print(corte2, corteB)			# Imprime na tela ao mesmo tempo que grava em arquivo - Ver linha abaixo:
		arqSaida.write(corte2 + '-' + corteB + '\n')

	arqSaida.close()				# Fecha arquivo de escrita (de saida)
	
	#arqFonte.close() - Nao precisa fechar arq aberto para leitura!!! Dá erro.

"""

(*) OBS - Este é o modelo de cada linha do arqFonte (.csv):

2017/10/12 00:00:00;('Vir', 'Virgo');13:53:23.08;-10:32:04.1;13:54:17.90;-10:37:02.8

"""

# Autor: Helio Giroto
