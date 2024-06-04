class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        temp = 0
        sum = 0
        sumList = [0]
        for num in nums:
            if num <= temp:
                sumList.append(sum)
                sum = num
            else:
                sum += num

            temp = num

        sumList.append(sum)
        return max(sumList)
            