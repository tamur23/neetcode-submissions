class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        _curr = 0
        for i in nums:
            if i == 1:
                _curr+=1
            else:
                _curr=0
                
            if _curr > _max:
                _max = _curr
        return _max

                    
        
        