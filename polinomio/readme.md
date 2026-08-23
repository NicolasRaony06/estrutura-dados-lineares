# Projeto Polinômio

Implementação de uma representação e manipulação de polinômios univariados utilizando **listas encadeadas**, desenvolvida em Python para a disciplina de Estrutura de Dados Lineares.

## 📋 Sobre a atividade

O projeto consiste em representar polinômios de uma variável por meio de uma lista encadeada.

Cada nó da lista representa um monômio do polinômio e armazena:

- coeficiente;
- grau;
- referência para o próximo nó.

A representação geral de um polinômio é:

```text
P(x) = anxⁿ + ... + a₂x² + a₁x + a₀
```

O projeto implementa operações matemáticas e estruturais sobre os polinômios, incluindo adição, subtração, multiplicação, avaliação, exibição e simplificação.

## 🎯 Objetivos

- Implementar uma lista encadeada em Python.
- Representar monômios por meio de nós.
- Representar polinômios utilizando listas encadeadas.
- Implementar operações entre polinômios.
- Utilizar sobrecarga de operadores em Python.
- Implementar a simplificação dos polinômios.
- Realizar a leitura das operações a partir de um arquivo de texto.
- Separar a estrutura de dados da lógica específica dos polinômios.

## 🧩 Estrutura do projeto

```text
polinomio/
│
├── README.md
├── main.py
│
├── estruturas/
│   ├── __init__.py
│   ├── no.py
│   └── lista.py
│
├── polinomio/
│   ├── __init__.py
│   └── polinomio.py
│
└── data/
    └── entrada.txt
```

### `main.py`

Ponto de entrada da aplicação.

É responsável por:

- ler o arquivo de entrada;
- interpretar as operações;
- criar e manipular os objetos `Polinomio`;
- apresentar os resultados.

### `estruturas/no.py`

Contém a classe responsável por representar um nó da lista encadeada.

Cada nó armazena:

```text
coeficiente
grau
próximo nó
```

### `estruturas/lista.py`

Contém a implementação da lista encadeada utilizada para armazenar os termos dos polinômios.

A lista é responsável pelas operações estruturais necessárias para manipulação dos nós.

### `polinomio/polinomio.py`

Contém a classe `Polinomio` e as operações específicas relacionadas à representação matemática dos polinômios.

### `data/entrada.txt`

Arquivo de texto utilizado como entrada para o programa.

## ⚙️ Operações

O projeto contempla as seguintes operações:

| Operação | Descrição |
|---|---|
| `G` | Retorna o grau do polinômio |
| `T` | Retorna a quantidade de termos |
| `+` | Adiciona dois polinômios |
| `-` | Subtrai dois polinômios |
| `*` | Multiplica dois polinômios |
| `A` | Avalia o polinômio para determinado valor de `x` |
| `P` | Exibe o polinômio em formato textual |
| Simplificação | Combina termos de mesmo grau e remove coeficientes zero |

As operações de adição, subtração e multiplicação são disponibilizadas por meio da sobrecarga dos operadores `+`, `-` e `*`, conforme especificado na atividade.

A operação de exibição também pode ser disponibilizada pela representação textual do objeto, utilizando os recursos de sobrecarga de operadores do Python.

## 🔢 Representação

Considere o polinômio:

```text
P(x) = -7x⁵ + 2x³ + 5.3x - 2
```

Sua representação por lista encadeada pode ser visualizada como:

```text
[-7, 5]
   ↓
[2, 3]
   ↓
[5.3, 1]
   ↓
[-2, 0]
   ↓
None
```

Cada elemento representa:

```text
[coeficiente, grau]
```

A lista deve manter os termos organizados de acordo com o grau dos monômios.

## ➕ Simplificação

A simplificação é responsável por unificar monômios que possuem o mesmo grau e remover monômios cujo coeficiente seja igual a zero.

Por exemplo:

```text
p(x) = 2x² - 4x + 1

q(x) = -3x⁴ + 5x² + 4x - 10
```

A soma inicialmente pode produzir:

```text
-3x⁴ + 2x² + 5x² - 4x + 4x + 1 - 10
```

Após a simplificação:

```text
-3x⁴ + 7x² - 9
```

Essa etapa é necessária após operações que possam produzir termos de mesmo grau.

## 📥 Entrada

Os dados utilizados pelo programa devem ser obtidos a partir de um arquivo de texto.

O arquivo deve conter, em cada linha, um polinômio ou uma operação a ser realizada sobre os polinômios.

A atividade utiliza esse arquivo para realizar operações como:

- adição de polinômios;
- obtenção do grau;
- exibição;
- avaliação.



## 🧪 Exemplo de avaliação

Considere:

```text
p(x) = -2x² + 4x
```

Para:

```text
x = 3
```

o resultado esperado é:

```text
p(3) = -2 × (3)² + 4 × (3)
p(3) = -42
```

## 🛠️ Tecnologias

- Python 3
- Estruturas de dados
- Lista encadeada
- Programação Orientada a Objetos
- Sobrecarga de operadores
- Manipulação de arquivos

## ▶️ Execução

A partir do diretório `polinomio/`, execute:

```bash
python main.py
```

Em ambientes onde o comando `python` aponta para uma versão diferente do Python 3:

```bash
python3 main.py
```

## 📚 Contexto acadêmico

**Disciplina:** Estrutura de Dados Lineares  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas  
**Instituição:** IFRN  
**Professor:** Aluísio Igor

Este projeto corresponde à atividade **Projeto Polinômio**, da segunda lista de exercícios da disciplina.