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
            if pilha.top().valor == pares[finded - 1]:
                pilha.pop()
                continue
            desbalanceamento_encontrado.extend([index, pares[pares.find(pilha.top().valor) + 1]])

    if pilha.vazia():
        return True
    return False, desbalanceamento_encontrado

if __name__ == "__main__":
    string = input("Escreva a expressão a ser verificada: ")
    resultado = balanceador(string)
    
    print(resultado)