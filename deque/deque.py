class Item:
    def __init__(self, valor, next = None, prev = None):
        self.valor = valor 
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
    
    def getInicio(self):
        return self.__inicio

    def getFim(self):
        return self.__fim

    def inserirInicio(self, valor):
        item = Item(valor, self.__inicio)

        if not self.__inicio:
            self.__inicio = item
            self.__fim = item
            return
        
        self.__inicio.prev = item
        self.__inicio = item

    def inserirFim(self, valor):
        item = Item(valor, None, self.__fim)

        if not self.__fim:
            self.__inicio = item
            self.__fim = item
            return
        
        self.__fim.next = item
        self.__fim = item
    
    def removerInicio(self):
        self.__inicio = self.__inicio.next

    def removerFim(self):
        self.__fim = self.__fim.prev
        self.__fim.next = None

if __name__ == "__main__":
    deque = Deque()

    print()
    deque.inserirFim(7)
    print(deque.getInicio().valor)
    print(deque.getFim().valor)

    print()
    deque.inserirInicio(2)
    print(deque.getInicio().valor)
    print(deque.getFim().valor)

    print()
    deque.inserirInicio(3)
    print(deque.getInicio().valor)
    print(deque.getFim().valor)

    print()
    deque.inserirFim(4)
    print(deque.getInicio().valor)
    print(deque.getFim().valor)

    print()
    deque.removerFim()
    print(deque.getInicio().valor)
    print(deque.getFim().valor)

    print()
    item = deque.getInicio()
    while item:
        print(item.valor)
        item = item.next

