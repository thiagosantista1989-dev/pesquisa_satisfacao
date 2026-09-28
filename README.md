# 📊 Pesquisa de Satisfação – TudoWeb

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Atendimento](https://img.shields.io/badge/Atendimento-ao%20Cliente-F59E0B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 📌 Sobre o projeto

Script em **Python** criado para a empresa de marketing **TudoWeb** realizar uma pesquisa de opinião com seus clientes sobre o **atendimento prestado**. O programa coleta os dados de **50 entrevistados**, conta as respostas e exibe o resultado final na tela. 📋

## 🎯 Objetivo

Descobrir o grau de satisfação dos clientes com o atendimento da empresa, mostrando quantos avaliaram como **EXCELENTE** e quantos avaliaram como **RUIM**.

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3**
- 💻 **Visual Studio Code**
- 🐙 **Git e GitHub**

## 📋 Como funciona

Para cada entrevistado, o programa solicita:

| Dado | Descrição |
|---|---|
| 👤 Nome | Nome do entrevistado |
| 🎂 Idade | Idade do entrevistado (número) |
| ⭐ Opinião | Avaliação do atendimento (1, 2 ou 3) |

**Opções de opinião:**

| Código | Opinião |
|---|---|
| 1 | 😄 EXCELENTE |
| 2 | 🙂 BOM |
| 3 | 😞 RUIM |

Ao final das 50 entrevistas, o programa exibe:

- a) 😄 Quantidade de respostas **EXCELENTE**
- b) 😞 Quantidade de respostas **RUIM**

> 💡 Se o entrevistado digitar um número diferente de 1, 2 ou 3, o programa avisa "Opção inválida!".

## 🧠 Conceitos utilizados

- 🔁 **Estrutura de repetição:** `for` com `range(50)` para repetir a coleta para cada entrevistado.
- 🔀 **Estruturas de decisão:** `if / elif / else` para verificar a opinião.
- ➕ **Contadores:** variáveis que somam cada tipo de resposta.

## ▶️ Como executar

1. Instale o [Python](https://www.python.org/downloads/) no computador.
2. Clone este repositório:
```bash
   git clone https://github.com/thiagosantista1989-dev/pesquisa_satisfacao.git
```
3. Entre na pasta do projeto:
```bash
   cd pesquisa_satisfacao
```
4. Execute o programa:
```bash
   python pesquisa.py
```
5. Informe nome, idade e opinião (`1`, `2` ou `3`) de cada entrevistado.

## 💻 Exemplo de uso

```
Entrevistado 10
Nome: joao
Idade: 22
Opinião (1-EXCELENTE, 2-BOM, 3-RUIM): 2

--- RESULTADO DA PESQUISA ---
Respostas EXCELENTE: 4
Respostas RUIM: 3
```

## ✅ Testes realizados

Teste feito com **10 entrevistados**:

| Nº | Nome | Idade | Opinião |
|---|---|---|---|
| 1 | Ana | 25 | 1 – Excelente |
| 2 | Bruno | 30 | 2 – Bom |
| 3 | Carla | 41 | 3 – Ruim |
| 4 | Diego | 19 | 1 – Excelente |
| 5 | Elisa | 52 | 1 – Excelente |
| 6 | Fábio | 33 | 3 – Ruim |
| 7 | Gina | 27 | 2 – Bom |
| 8 | Hugo | 45 | 1 – Excelente |
| 9 | Iara | 38 | 3 – Ruim |
| 10 | João | 22 | 2 – Bom |

**Resultado obtido:** 4 respostas EXCELENTE e 3 respostas RUIM ✔️

## 📁 Estrutura do projeto

```
pesquisa_satisfacao/
├── README.md
├── pesquisa.py
└── prints/
    ├── codigo.png
    └── execucao.png
```

## 👨‍💻 Autor

Feito por **Thiago Souza** 💙

📚 Atividade da Agenda 8 – Desenvolvimento de Sistemas
