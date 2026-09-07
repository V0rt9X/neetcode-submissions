class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
            
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            if finder == slow:
                return finder