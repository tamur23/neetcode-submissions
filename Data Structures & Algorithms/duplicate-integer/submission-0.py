class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        
        for i in nums:
            if i in _set:
                return True
            else:
                _set.add(i)
        return False