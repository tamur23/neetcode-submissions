class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _ret = []
        _product = 1
        #left product
        for i,x in enumerate(nums):
            _ret.append(_product)
            _product*=x
        
        #right sum
        _product = 1
        _rev_index = len(_ret)-1
        for x in reversed(nums):
            _ret[_rev_index]*=_product
            _product*=x
            _rev_index -= 1
        return _ret