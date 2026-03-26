# Code Interview – Estruturas de Dados

## 1) Problema com Pilha (Stack)

**Nome do problema:**
Valid Parentheses

**Link:**
https://leetcode.com/problems/valid-parentheses/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Pilha (Stack)

**Justificativa:**
A pilha é ideal para esse problema porque segue o princípio LIFO (Last In, First Out). Ao percorrer a string, cada caractere de abertura é empilhado. Quando aparece um caractere de fechamento, verifica-se se ele corresponde ao último elemento inserido na pilha. Isso garante a validação correta da ordem e do balanceamento dos parênteses.

---

## 2) Problema com Array 1

**Nome do problema:**
Best Time to Buy and Sell Stock

**Link:**
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Array

**Justificativa:**
O problema envolve analisar um array de preços ao longo do tempo para determinar o maior lucro possível com uma única compra e venda. O uso de array é adequado porque os dados representam uma sequência temporal, permitindo percorrer os valores uma única vez e manter o menor preço encontrado até o momento, calculando o lucro máximo de forma eficiente (O(n)).

---

## 3) Problema com Array 2

**Nome do problema:**
Maximum Subarray

**Link:**
https://leetcode.com/problems/maximum-subarray/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Array

**Justificativa:**
Esse problema utiliza arrays para encontrar a sublista contínua com maior soma. A estrutura é adequada porque permite percorrer os elementos de forma sequencial, aplicando o algoritmo de Kadane, que resolve o problema de forma eficiente com complexidade O(n).

---

## 4) Problema com Lista Encadeada 1

**Nome do problema:**
Linked List Cycle

**Link:**
https://leetcode.com/problems/linked-list-cycle/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Lista Encadeada

**Justificativa:**
Esse problema envolve verificar se uma lista encadeada possui um ciclo, ou seja, se algum nó aponta para um nó anterior na estrutura. A lista encadeada é essencial aqui, pois o desafio depende da navegação entre os nós por meio de ponteiros. A solução mais eficiente utiliza dois ponteiros (lento e rápido), explorando a estrutura dinâmica da lista sem necessidade de memória adicional, com complexidade O(n).


