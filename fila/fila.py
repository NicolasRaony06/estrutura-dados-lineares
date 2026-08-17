class Item:
    def __init__(self, valor, prev):
        self.valor = valor
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.valor}"

class Fila:
    def __init__(self):
        self.__primeiro = None

    def inserir(self, valor):
        pass

    def excluir(self):
        pass