#Problema 1 - Pilha
# Nome do problema:Validação de Parenteses
# Link:https://leetcode.com/problems/valid-parentheses/
# Plataforma:LeetCode
#########

# Dada uma string contendo apenas os caracteres '(', ')', '{', '}', '['e ']',
# determine se a string de entrada é válida.

#Uma sequência de entrada é válida se:

#Os colchetes abertos devem ser fechados pelo mesmo tipo de colchetes.
#Os colchetes abertos devem ser fechados na ordem correta.
#Cada parêntese fechado tem um parêntese aberto correspondente do mesmo tipo.

# Solução sem IA
class Solution:
    def isValid(self, s: str) -> bool:
        mudou = True

        while mudou:
            mudou = False

            if "()" in s:
                s = s.replace("()", "")
                mudou = True

            if "[]" in s:
                s = s.replace("[]", "")
                mudou = True

            if "{}" in s:
                s = s.replace("{}", "")
                mudou = True

        return s == ""
        

# Solução com IA
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pares = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pares:  # é um fechamento
                if not stack or stack[-1] != pares[char]:
                    return False
                stack.pop()
            else:  # é uma abertura
                stack.append(char)

        return len(stack) == 0

#Vantagem sobre o código sem IA:

#Código sem IA: Faz várias substituições → mais lento

#Código com IA: Resolve em uma passada só e escala melhor para entradas grandes (até 10⁴)