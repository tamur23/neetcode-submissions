class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _seen = {}
        
        for i, x in enumerate(nums):
            _y = target - x
            if _y in _seen:
                return [_seen[_y], i]
            _seen[x] = i
        
        return []


