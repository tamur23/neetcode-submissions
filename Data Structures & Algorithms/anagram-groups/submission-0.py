class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _sorted_map = {}

        for s in strs:
            _key = ''.join(sorted(s))
            _sorted_map.setdefault(_key, []).append(s)
        
        return list(_sorted_map.values())
