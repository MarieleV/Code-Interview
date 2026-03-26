height3 = [1,8,6,2,5,4,8,3,7]
height4 = [-4,3,2,1,4]
height5 = [7.7, 3.3, 2.2, 1.1, 4.4]
height = [1,"8",6,2,5,4,8,3,7]


left = 0
right = len(height) - 1
area = 0

while left < right:
    h = min(height[left], height[right])
    area = max(area, h * (right - left))

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("teste numeros com string: ", height)
print(area)
#print("Desafio proposto pelo LeetCode: https://leetcode.com/problems/container-with-most-water/")
#print("output esperado: 49")
#print("output obtido: ", area) 