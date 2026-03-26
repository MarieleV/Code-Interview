#Problema de Listas

# Sem IA
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitados = []
        
        atual = head
        while atual is not None:
            if atual in visitados:
                return True
            
            visitados.append(atual)
            atual = atual.next
        
        return False

# Com IA
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lento = head
        rapido = head
        
        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next
            
            if lento == rapido:
                return True
        
        return False