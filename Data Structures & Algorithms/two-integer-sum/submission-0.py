class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            otherN = target - num
            if otherN in hashmap:
                return[hashmap[otherN], i]
            
            hashmap[num] = i