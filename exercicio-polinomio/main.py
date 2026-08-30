from polinomio import Polinomio

def stringParaPolinomio(polinomioStr:str):
    '''Recebe uma string no formato 'coefiente grau...' e converte para um objeto de Polinomio. Retorna um objeto de Polinomio.'''
    if len(polinomioStr) < 2:
        return int(polinomioStr)

    polinomioStr = polinomioStr.split(' ')
    polinomio = Polinomio()
    for i, numero in enumerate(polinomioStr):
        if i % 2 == 0:
            polinomio.inserirTermo(float(numero), int(polinomioStr[i+1]))
    return polinomio

def lerArquivo(caminho_arquivo:str = None):
    '''Procura por padrão um arquivo .txt em /data, caso não seja especificado um caminho. Retorna um dicionário contendo as instruções e os polinomios.'''
    if not caminho_arquivo:
        from glob import glob
        caminho_arquivo = (glob("data/*.txt"))[0]

    instrucoes = {}
    comandos = ('g', 't', '+', '-', '*', 'a', 'p')
    with open(caminho_arquivo) as arquivo:
        instrucao_prev = ''
        for index, line in enumerate(arquivo):
            if line.strip().lower() in comandos:
                instrucoes[f"instrucao{index}"] = {
                    'comando': line.strip().lower(), 
                    'polinomios': []
                    }
                instrucao_prev = f"instrucao{index}"
                continue
            instrucoes[instrucao_prev]['polinomios'].append(stringParaPolinomio(line.strip().lower().rstrip('\n')))
    return instrucoes

def executar():
    caminho_arquivo = input("Digite o caminho do arquivo .txt (Deixe em branco para o utilizar o padrão em /data):")

    instrucoes = lerArquivo(caminho_arquivo)
    resultados = []
    for instrucao in instrucoes.values():
        match instrucao['comando']:
            case '+':
                polinomio = instrucao['polinomios'][0] + instrucao['polinomios'][1]
                resultados.append(polinomio)
            case '-':
                polinomio = instrucao['polinomios'][0] - instrucao['polinomios'][1]
                resultados.append(polinomio)
            case '*':
                polinomio = instrucao['polinomios'][0] * instrucao['polinomios'][1]
                resultados.append(polinomio)
            case 'g':
                resultados.append(instrucao['polinomios'][0].grau())
            case 't':
                resultados.append(instrucao['polinomios'][0].tamanho())
            case 'a':
                polinomio = instrucao['polinomios'][1].definirX(instrucao['polinomios'][0])
                resultados.append(polinomio)
            case 'p':
                resultados.append(str(instrucao['polinomios'][0]))
    return resultados

if __name__ == "__main__":
    resultados = executar()
    for resultado in resultados:
        print(resultado)

