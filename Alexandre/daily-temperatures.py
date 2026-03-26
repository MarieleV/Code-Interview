temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures2 = [-1, -2, -3, -1, -5]
temperatures3 = ["30", "40", "50", "20", "10", "25", "60", "35"]
temperatures4 = [100, 90, 80, 70, 60, 50, 40, 30]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer
#print("Desafio proposto pelo LeetCode: https://leetcode.com/problems/daily-temperatures/")
#print("output esperado: [1, 1, 4, 2, 1, 1, 0, 0]")
print("Teste com temperatura nunca sendo maior: ")
print("temperaturas: ", temperatures4)
print("output obtido: ", Solution().dailyTemperatures(temperatures4))