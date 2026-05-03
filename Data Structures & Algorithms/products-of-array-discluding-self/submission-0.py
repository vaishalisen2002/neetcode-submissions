class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0]*(len(nums))
        postfix = [0]*(len(nums))

        prefix[0]= 1
        postfix[len(postfix)-1]= 1

        final = []

        prod1 = 1
        prod2 = 1

        for i in range(1, len(nums)):
            prod1 = prod1 * nums[i-1]
            prefix[i] = prod1
        for i in range(len(prefix)-2, -1,-1):
            prod2 = prod2 * nums[i+1]   
            postfix[i] = prod2
        for i in range(0, len(nums)):
            final.append(prefix[i]*postfix[i])

        return final    
