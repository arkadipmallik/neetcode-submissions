from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result=[]
        for i in strs:
            sorted_strs = tuple(sorted(i))
            anagram_map[sorted_strs].append(i)
        for value in anagram_map.values():
            result.append(value)
        return result
            