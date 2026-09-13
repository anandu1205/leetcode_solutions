class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        currMax=maxSum=nums[0]
        currMin=minSum=nums[0]
        n=len(nums)
        for i in range(1,n):
            currMax=max(nums[i],currMax+nums[i])
            maxSum=max(maxSum,currMax)

            currMin=min(nums[i],currMin+nums[i])
            minSum=min(minSum,currMin)

        if maxSum<0:
            return maxSum
        circular_sum=total_sum-minSum
        return max(maxSum,circular_sum)
            
        