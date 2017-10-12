
######################################################################

#       ESTE PROGRAMA PYTHON SIMULA O COMANDO CAT DO LINUX           #

######################################################################

arq = open('frutas.txt').read()
print(arq)


'''
arq='frutas.txt'
with open(arq, 'r') as arquivo:     # Abre o arquivo escolhido na linha acima...
    for linha in arquivo:           # Para cada linha neste arquivo...
        print(linha)                # Imprime linha
        #input()                    # Pode descomentar para dar uma pausa a cada linha impressa...


O Arquivo frutas.txt pode ser visualizado em:
https://raw.githubusercontent.com/HelioGiroto/Dict_PySh/master/frutas.txt
'''
