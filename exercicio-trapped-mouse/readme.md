# Trapped Mouse

Implementação em Python de um algoritmo de **backtracking utilizando uma pilha (Stack)** para encontrar a saída de um labirinto.

O projeto faz parte das atividades da disciplina de **Estruturas de Dados Lineares** e tem como objetivo aplicar o conceito de **Pilha (Stack)** na resolução de um problema de busca em um labirinto.

## Objetivo

O programa recebe um labirinto representado por caracteres e procura um caminho entre a entrada (`m`) e a saída (`e`).

Durante a busca:

* células já visitadas são marcadas com `.`;
* caminhos possíveis são armazenados em uma pilha;
* quando um caminho chega a um beco sem saída, o algoritmo utiliza a pilha para retornar a uma possibilidade ainda não explorada;
* caso não exista nenhum caminho possível, o programa informa que a saída não pode ser encontrada.

A busca utiliza a seguinte ordem de exploração:

1. Direita
2. Esquerda
3. Baixo
4. Cima

Como a `Stack` utiliza o princípio **LIFO (Last In, First Out)**, os vizinhos são inseridos na ordem necessária para que sejam retirados respeitando a sequência de exploração definida.

## Representação do labirinto

O arquivo de entrada utiliza os seguintes caracteres:

| Caractere | Significado                       |
| --------- | --------------------------------- |
| `0`       | Caminho livre                     |
| `1`       | Parede                            |
| `m`       | Entrada / posição inicial do rato |
| `e`       | Saída                             |
| `.`       | Posição já visitada               |

As paredes externas do labirinto são adicionadas automaticamente durante a montagem da estrutura interna.

### Exemplo

Arquivo de entrada:

```text
00m0
0111
01e0
0000
```

A estrutura interna recebe uma borda de paredes:

```text
111111
100m01
101111
101e01
100001
111111
```

## Estrutura do projeto

```text
trapped_mouse/
├── README.md
├── cell.py
├── maze.py
├── stack.py
├── main.py
└── arquivos/
    └── labirinto1.txt
```

### `cell.py`

Define a classe `Cell`, utilizada para representar uma posição no labirinto por meio das coordenadas `x` e `y`.

### `stack.py`

Implementa a estrutura de dados **Pilha (Stack)** utilizando nós encadeados.

A pilha fornece as operações necessárias para o algoritmo de backtracking:

* `push()`
* `pop()`
* `top()`

### `maze.py`

Contém a classe `Maze`, responsável pela montagem e resolução do labirinto.

Entre suas responsabilidades estão:

* montar o labirinto a partir do arquivo;
* adicionar as paredes externas;
* localizar a entrada e a saída;
* obter as células vizinhas;
* verificar quais vizinhos podem ser visitados;
* marcar células como visitadas;
* armazenar possibilidades na pilha;
* realizar o backtracking;
* realizar opcionalmente uma animação da busca.

### `main.py`

Responsável por criar o objeto `Maze`, carregar o arquivo e executar a busca pela saída.

## Funcionamento do algoritmo

O processo de resolução pode ser representado da seguinte maneira:

```text
Entrada
   │
   ▼
Marcar célula atual como visitada
   │
   ▼
Obter células vizinhas
   │
   ▼
Verificar vizinhos válidos
   │
   ▼
Adicionar possibilidades à Stack
   │
   ▼
Existe alguma possibilidade?
   │
   ├── Não ──► Não existe caminho
   │
   └── Sim
          │
          ▼
       POP da Stack
          │
          ▼
    Nova célula atual
          │
          ▼
       Repetir
```

O processo continua até que:

```text
currentCell == exitCell
```

Quando isso acontece, a célula de saída é retornada.

## Backtracking

A `mazeStack` armazena células que representam possibilidades de caminhos ainda não exploradas.

Por exemplo:

```text
          A
        /   \
       B     C
```

Ao encontrar os caminhos `B` e `C`, uma das possibilidades é escolhida e a outra permanece armazenada na pilha.

Caso o caminho escolhido resulte em um beco sem saída, o algoritmo utiliza `pop()` para recuperar uma possibilidade anterior:

```text
A → B → beco
    │
    └── backtracking
           ↓
           C
```

A utilização da marcação `.` evita que posições já visitadas sejam exploradas novamente.

## Execução

No `main.py`, o labirinto pode ser carregado e resolvido da seguinte forma:

```python
from maze import Maze

maze = Maze()

maze.start(maze_file="arquivos/labirinto1.txt")

result = maze.exit()

if result:
    print(f"Exit successfully found, Cell: {result}")
    print(maze)
else:
    print("There is no possible exit in the maze")
    print(maze)
```

Para executar:

```bash
python main.py
```

## Animação

O método de resolução possui um parâmetro opcional para visualizar o processo de busca no terminal:

```python
maze.exit(animated=True)
```

Com a animação habilitada, o estado atual do labirinto é exibido a cada movimento, permitindo acompanhar a exploração e o backtracking.

Sem animação:

```python
maze.exit()
```

A resolução é executada normalmente sem a pausa entre os movimentos.

## Exemplo de resultado

Durante a execução, as posições visitadas podem aparecer como:

```text
111111
1...01
101..1
10.e.1
100001
111111
```

As células `.` representam posições que já foram exploradas durante a busca.

Quando a saída é encontrada, o método retorna a `Cell` correspondente à posição de `e`.

## Conceitos utilizados

Este projeto aplica principalmente:

* **Pilha (Stack)**
* **LIFO (Last In, First Out)**
* **Lista encadeada**
* **Backtracking**
* **Busca em uma estrutura bidimensional**
* **Manipulação de strings**
* **Programação Orientada a Objetos**
* **Composição entre classes**
* **Representação de coordenadas com objetos `Cell`**

## Atividade

Projeto desenvolvido como prática da disciplina de **Estruturas de Dados Lineares**, com foco na aplicação da estrutura de dados **Pilha** em um algoritmo de busca com backtracking.
