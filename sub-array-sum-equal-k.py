class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        c_sum = {0:1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            if current_sum-k in c_sum:
                count += c_sum[current_sum-k]
            c_sum[current_sum] = c_sum.get(current_sum, 0)+1

        return count
        
