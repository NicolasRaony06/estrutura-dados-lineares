from estrutura.pilha import Pilha

def balanceador(string:str):
    pilha = Pilha()
    pares = "(){}[]"
    desbalanceamento_encontrado = []
    for index, char in enumerate(string):
        finded = pares.find(char)
        if finded < 0:
            continue
        elif finded % 2 == 0:
            pilha.push(char)
            continue
        else:
            if not pilha.vazia():
                if pilha.top().valor == pares[finded - 1]:
                    pilha.pop()
                    continue
            desbalanceamento_encontrado.append((index, pares[finded - 1]))

    if not pilha.vazia():
        no = pilha.top()
        while no:
            finded = pares.find(no.valor)
            desbalanceamento_encontrado.append((len(string) - pilha.tamanho(), pares[finded + 1]))
            no = no.prev
            pilha.pop()
    
    if len(desbalanceamento_encontrado) == 0:
        return True
    return False, desbalanceamento_encontrado

if __name__ == "__main__":
    string = input("Escreva a expressão a ser verificada: ")
    resultado = balanceador(string)
    print(resultado)