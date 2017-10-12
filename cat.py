
######################################################################

#       ESTE PROGRAMA PYTHON SIMULA O COMANDO CAT DO LINUX           #

######################################################################


arq='frutas.txt'
with open(arq, 'r') as arquivo:     # Abre o arquivo escolhido na linha acima...
    for linha in arquivo:           # Para cada linha neste arquivo...
        print(linha)                # Imprime linha
        #input()                    # Pode descomentar para dar uma pausa a cada linha impressa...
