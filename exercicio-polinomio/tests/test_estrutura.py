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

#teste de exclusão
print()
lista.excluir(2, 3)
lista.excluir(6, 6)
lista.excluir(5.3, 1)
lista.excluir(0, 0)

for no in lista.mostrarAll():
    print(no, '\n')
# - fim -

#teste método existe
print(lista.existe(5,5))
print(lista.existe(5, 9))
# -- fim --

