** ALTERNTIVA PYTHON DO COMANDO SORT | UNIQ (ou sort -u) NO PYTHON: **

Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> canasta = ['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'banana', 'pera', 'pera']
>>> len(canasta)
9
>>> canasta_sem_repetir=set(canasta)
>>> len(canasta_sem_repetir)
4
>>> canasta_sem_repetir
{'naranja', 'banana', 'manzana', 'pera'}
>>> >>> canasta.count('banana')
2
>>> canasta
['manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'banana', 'pera', 'pera']
>>> 

