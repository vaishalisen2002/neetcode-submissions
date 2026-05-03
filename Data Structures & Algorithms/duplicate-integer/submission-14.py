class Solution:
    def hasDuplicate(self, nums: List[int])-> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
               return True
            hashset.add(n)
        return False

sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4]))  # False
print(sol.hasDuplicate([1, 2, 3, 1]))  # True