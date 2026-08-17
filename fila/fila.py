class Item:
    def __init__(self, valor, next = None):
        self.valor = valor
        self._next = next

    def __str__(self) -> str:
        return f"{self.valor}"

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def inicio(self):
        return self.__inicio

    def fim(self):
        return self.__fim

    def inserir(self, valor):
        item = Item(valor)
        if not self.__inicio:
            self.__inicio = item
            self.__fim = item
            return

        self.__fim._next = item
        self.__fim = item

    def excluir(self):
        if self.__inicio:
            self.__inicio = self.__inicio._next
            if not self.__inicio:
                self.__fim = None


if __name__ == "__main__":
    fila = Fila()

    fila.inserir(3)
    print(fila.inicio())
    print(fila.fim(), "\n")

    fila.inserir(4)
    print(fila.inicio())
    print(fila.fim(), "\n")

    fila.inserir(5)
    print(fila.inicio())
    print(fila.fim(), "\n")

    item = fila.inicio()
    while True:
        if item:
            print(item.valor)
            item = item._next
            continue
        break

    print()
    fila.excluir()
    print(fila.inicio())
    print(fila.fim(), "\n")

    fila.excluir()
    print(fila.inicio())
    print(fila.fim(), "\n")
    
    fila.excluir()
    print(fila.inicio())
    print(fila.fim(), "\n")
