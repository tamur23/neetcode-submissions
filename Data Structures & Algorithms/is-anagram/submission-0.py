class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        _s_map = {}
        for _s in s:
            _s_map[_s] = _s_map.get(_s, 0) + 1
        
        for _t in t:
            if _t not in _s_map:
                return False
            else:
                if _s_map[_t] > 0:
                    _s_map[_t] -= 1
                else:
                    return False
        
        return True



        