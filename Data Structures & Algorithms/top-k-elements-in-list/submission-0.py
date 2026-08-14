class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = {}
        for i in nums:
            _dict[i] = _dict.get(i, 0) + 1
        
        return sorted(_dict, key=_dict.get, reverse=True)[:k]