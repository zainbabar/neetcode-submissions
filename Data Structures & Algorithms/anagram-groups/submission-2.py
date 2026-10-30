from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letter_counts = [0] * 26
            for c in s:
                letter_counts[ord(c) - 97] += 1
            # lists arent hashable so turn the counts into a tuple for the key
            anagrams[tuple(letter_counts)].append(s)
        return list(anagrams.values())