from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_letter_counts = []
        for s in strs:
            letter_counts = [0] * 26
            for i in range(len(s)):
                pos = ord(s[i]) - 97
                letter_counts[pos] += 1
            strs_letter_counts.append(letter_counts)
        
        # so now we have a list of lists for each string
        # each inner list has the character frequencies for each word
        # anagrams have the same character frequencies
        # lists arent hashable to convert them to tuples for hashing
        strs_letter_counts = [tuple(x) for x in strs_letter_counts]
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            key = strs_letter_counts[i] # the hash is the same for anagrams
            word = strs[i]
            anagrams[key].append(word)
        
        output = []
        for key in anagrams:
            output.append(anagrams[key])
        
        return output


            


        