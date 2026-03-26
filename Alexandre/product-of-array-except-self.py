nums = [1,2,3,4]
nums3 = ["1",2,3,4]
nums2 = [2.2,2.5,2.5,2.5]

# resp = [1] * len(nums)

# for i in range(len(nums)):
#     if i < len(nums) - 1:
#         ini = nums[i] * nums[i + 1]
#         resp[i] = ini

# for i in range(len(nums) - 1, -1, -1):
#     fim = nums[i] * nums[i - 1]
#     resp[i] = resp[i] * fim

# print(resp)


        
n = len(nums) 
resp = [1] * n 

esq = 1 
for i in range(n):
    resp[i] = esq
    esq *= nums[i]
            
der = 1
for i in range(n -1,-1,-1):
    resp[i] *= der
    der *= nums[i]
print("Desafio proposto pelo LeetCode: https://leetcode.com/problems/product-of-array-except-self/")
print("output esperado: [24, 12, 8, 6]")
print("output obtido: ", resp) 
