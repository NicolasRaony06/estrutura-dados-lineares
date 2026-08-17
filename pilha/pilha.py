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
        return self.__top

    def __push(self, valor):
        item = Item(valor, self.__top)
        self.__top = item 

    def push(self, valor):
        if not self.__tamanho:
            self.__push(valor)
            return
        
        if self.__tamanho > self.__tamanho_contador:
            self.__push(valor)
            self.__tamanho_contador += 1
                
    def pop(self):
        if self.__top:
            item_prev = self.__top.prev
            self.__top = item_prev

    def vazia(self):
        if not self.__top:
            return True
        
    def cheia(self):
        if self.__tamanho_contador == self.__tamanho:
            return True
        

if __name__ == "__main__":
    pilha = Pilha(3)

    pilha.push(1)
    pilha.push(2)
    pilha.push(3)

    print(pilha.top())
    pilha.pop()
    print(pilha.top())  

    print(pilha.cheia())
    print(pilha.vazia())
    

    
        
        
