# Problema 2 de Array:
#Dado um array de inteiros nums, encontre o subarray com a maior soma, e retorne sua soma .


# Sem IA
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maior_soma = nums[0]

        for i in range(n):
            soma_atual = 0
            for j in range(i, n):
                soma_atual += nums[j]
                
                if soma_atual > maior_soma:
                    maior_soma = soma_atual

        return maior_soma
    
# Com IA
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soma_atual = nums[0]
        maior_soma = nums[0]

        for i in range(1, len(nums)):
            # decide: continua somando ou começa do zero?
            soma_atual = max(nums[i], soma_atual + nums[i])
            
            # atualiza o maior valor encontrado
            maior_soma = max(maior_soma, soma_atual)

        return maior_soma