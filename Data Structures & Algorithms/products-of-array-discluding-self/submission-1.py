class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _zeros=[]
        _product=1
        for i, x in enumerate(nums):
            if x == 0: _zeros.append(i)
            else: _product *= x
        
        _ret = []
        if len(_zeros) > 1: _product = 0
        for x in nums:
            if x == 0:
                _ret.append(_product)
            else:
                if len(_zeros): _ret.append(0)
                else: _ret.append(int(_product/x))
        return _ret
