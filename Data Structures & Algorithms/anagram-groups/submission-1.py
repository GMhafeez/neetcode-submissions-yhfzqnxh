class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        result = []

        for s in strs:
            sorted_S = tuple(sorted(s))
            maps[sorted_S].append(s)
        
        for value in maps.values():
            result.append(value)


        return result