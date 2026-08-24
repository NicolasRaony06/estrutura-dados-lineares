from estruturas.lista_encadeada import Lista

# teste de inserção e ordenação da lista encadeada
lista = Lista()

lista.inserir(5, 5)
lista.inserir(5.3, 1)
lista.inserir(2, 3)
lista.inserir(6, 6)
lista.inserir(2, 3)
lista.inserir(2, 3)

for no in lista.mostrarAll():
    print(no, '\n')
# -- fim --
