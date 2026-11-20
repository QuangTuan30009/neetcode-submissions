class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            sorted_cha = sorted(word)
            label = "".join(sorted_cha)
            bucket = group[label]
            bucket.append(word)
        result = list(group.values())
        return result
