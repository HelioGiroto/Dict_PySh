######################################################################

#       ESTE PROGRAMA PYTHON SIMULA O COMANDO CUT DO LINUX           #

######################################################################


arq='frutas.txt'                      # Escolhe o arquivo

with open(arq, 'r') as arquivo:
    for linha in arquivo:             # A cada linha do arquivo...
        preco=linha.split('	')[1]     # Divide (separa) a linha em varias partes usando o delimitador TAB ('  ') e captura apenas o campo número [1] - ou seja o 2º do array
        print(preco)                  # Imprime esse campo (o campo preço)

'''
O Arquivo frutas.txt pode ser visualizado em:
https://raw.githubusercontent.com/HelioGiroto/Dict_PySh/master/frutas.txt
'''
