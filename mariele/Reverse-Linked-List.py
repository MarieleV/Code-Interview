#Problema de Listas

# Sem IA
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        valores = []
    
        atual = head
        while atual:
            valores.append(atual.val)
            atual = atual.next
        
        valores.reverse()
        
        novo_head = None
        atual = None
        
        for valor in valores:
            if novo_head is None:
                novo_head = ListNode(valor)
                atual = novo_head
            else:
                atual.next = ListNode(valor)
                atual = atual.next
        
        return novo_head

# Com IA
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior = None
        atual = head
        
        while atual:
            proximo = atual.next  # guarda o próximo
            atual.next = anterior  # inverte o ponteiro
            anterior = atual       # avança anterior
            atual = proximo        # avança atual
        
        return anterior
