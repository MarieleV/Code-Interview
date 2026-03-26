# Problema 1 de Array
# Best Time to Buy and Sell Stock

# Com IA
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_preco = prices[0]
        max_lucro = 0

        for preco in prices:
            if preco < min_preco:
                min_preco = preco
            else:
                max_lucro = max(max_lucro, preco - min_preco)

        return max_lucro
    
# Sem IA
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_preco = prices[0]
        max_lucro = 0

        for preco in prices:
            if preco < min_preco:
                min_preco = preco
            else:
                max_lucro = max(max_lucro, preco - min_preco)

            min_preco = min(min_preco, preco)

        return max_lucro