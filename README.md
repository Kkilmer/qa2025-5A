# qa2025-5A

## 1. Descrição da Aplicação

A aplicação Calculadora de IMC (Índice de Massa Corporal) recebe o peso (em kg) e a altura (em metros) de uma pessoa e retorna:

- O valor do IMC calculado
- A classificação com base nas faixas da OMS (Organização Mundial da Saúde)

## 2. Regras de Negócio

- O IMC é calculado pela fórmula:

```IMC = peso / (altura ** 2)```

2.1 **Classificação do IMC (OMS)**

   | Faixa de IMC   | Classificação    |
   | -------------- | ---------------- |
   | Menor que 18.5 | Abaixo do peso   |
   | 18.5 – 24.9    | Peso normal      |
   | 25.0 – 29.9    | Sobrepeso        |
   | 30.0 – 34.9    | Obesidade grau 1 |
   | 35.0 – 39.9    | Obesidade grau 2 |
   | 40.0 ou mais   | Obesidade grau 3 |

2.2 **Validação de Dados**

   * Peso e altura devem ser **maiores que zero**.
   * Caso contrário, o programa deve lançar uma exceção `ValueError` com a mensagem:

     > "Peso e altura devem ser maiores que zero."

```

# Calculadora de IMC (Índice de Massa Corporal)

Aplicação simples em **Python** para cálculo e classificação do **IMC**, conforme os padrões da **OMS**.  
O projeto foi desenvolvido com foco em **clareza e testabilidade**, incluindo testes unitários com o módulo `unittest`.

---

## 🚀 Como Usar

Clone o repositório e execute o código Python:

```bash
git clone https://github.com/Kkilmer/qa2025-5A.git
cd qa2025-5A

calculadora-imc/
│
├── imc.py               # Módulo principal com funções de cálculo e classificação
├── test_imc.py          # Testes unitários
└── README.md            # Documentação do projeto

```

2. **Classificação do IMC (OMS)**

   | Faixa de IMC   | Classificação    |
   | -------------- | ---------------- |
   | Menor que 18.5 | Abaixo do peso   |
   | 18.5 – 24.9    | Peso normal      |
   | 25.0 – 29.9    | Sobrepeso        |
   | 30.0 – 34.9    | Obesidade grau 1 |
   | 35.0 – 39.9    | Obesidade grau 2 |
   | 40.0 ou mais   | Obesidade grau 3 |

3. **Validação de Dados**

   * Peso e altura devem ser **maiores que zero**.
   * Caso contrário, o programa deve lançar uma exceção `ValueError` com a mensagem:

     > "Peso e altura devem ser maiores que zero."


```

## Executando os Testes Unitários

Para executá-los:

```python3 -m unittest test_imc.py -v```


Saída esperada:

```
test_cal_imc_valido ... ok
testClassificacaoAbaixoPeso ... ok
testClassificacaoPesoNormal ... ok
testClassificacaoSobrepeso ... ok
testClassificacaoObesidadeGrau1 ... ok
testClassificacaoObesidadeGrau2 ... ok
testClassificacaoObesidadeGrau3 ... ok
testValoresInvalidos ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK


# Gerar um relatório no terminal
coverage report

---

## ✅ Regras de Negócio Testadas

O resultado é arredondado para **duas casas decimais**.  
 Teste responsável: `test_cal_imc_valido`

---

### 🔹 RN02 — Classificação: Abaixo do peso
Se o IMC for **menor que 18.5**, o resultado deve ser:
> “Abaixo do peso”  
 Teste responsável: `testClassificacaoAbaixoPeso`

---

### 🔹 RN03 — Classificação: Peso normal
Se o IMC estiver entre **18.5 e 24.9**, a classificação será:
> “Peso normal”  
 Teste responsável: `testClassificacaoPesoNormal`

---

### 🔹 RN04 — Classificação: Sobrepeso
Para valores entre **25.0 e 29.9**, a classificação é:
> “Sobrepeso”  
 Teste responsável: `testClassificacaoSobrepeso`

---

### 🔹 RN05 — Classificação: Obesidade grau 1
Se o IMC estiver entre **30.0 e 34.9**, o resultado é:
> “Obesidade grau 1”  
 Teste responsável: `testClassificacaoObesidadeGrau1`

---

### 🔹 RN06 — Classificação: Obesidade grau 2
Valores entre **35.0 e 39.9** indicam:
> “Obesidade grau 2”  
 Teste responsável: `testClassificacaoObesidadeGrau2`

---

### 🔹 RN07 — Classificação: Obesidade grau 3
Quando o IMC for **40.0 ou mais**, a saída deve ser:
> “Obesidade grau 3”  
Teste responsável: `testClassificacaoObesidadeGrau3`

---

### 🔹 RN08 — Validação de entradas
A aplicação só aceita **peso e altura maiores que zero**.  
Caso contrário, é lançada uma exceção:
> `ValueError: Peso e altura devem ser maiores que zero.`  
 Teste responsável: `testValoresInvalidos`

---

