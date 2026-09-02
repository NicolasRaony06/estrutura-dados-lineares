class Item:
    def __init__(self, valor, prev):
        self.valor = valor
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.valor}"

class Pilha:
    def __init__(self, tamanho : int = None):
        self.__top = None
        self.__tamanho = tamanho
        self.__tamanho_contador = 0

    def top(self):
        '''Retorna o ultimo nó adicionado.'''
        return self.__top

    def __push(self, valor):
        item = Item(valor, self.__top)
        self.__top = item 

    def push(self, valor):
        '''Recebe um valor, e adiciona um nó na ultima posição, topo.'''
        if not self.__tamanho:
            self.__push(valor)
            return
        
        if self.__tamanho > self.__tamanho_contador:
            self.__push(valor)
            self.__tamanho_contador += 1
                
    def pop(self):
        '''Retira o ulitmo nó adicionado, topo.'''
        if self.__top:
            item_prev = self.__top.prev
            self.__top = item_prev

    def vazia(self):
        if not self.__top:
            return True
        
    def cheia(self):
        if self.__tamanho_contador == self.__tamanho:
            return True
