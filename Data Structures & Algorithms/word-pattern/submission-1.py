from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # pattern is keys, word is value
        # first occurance of a letter in pattern sets the value
        # if another occurence of a word doesnt have that value 
        # then we have an issue... 
        bijections = {}
        # s is a string so split it into a list
        split_s =s.split()
        # right away if our pattern and string have a length mismatch then its wrong
        if len(split_s) != len(pattern):
            return False

        for char, word in zip(pattern, split_s):
            if bijections.get(char) is not None:
                # not none so a mapping exists
                # check if the actual word is the same as the mapping
                if bijections[char] == word:
                    continue
                # if its not that means 1 letter maps to two words
                else:
                    return False
            # no mapping yet so add one
            else:
                bijections[char] = word 
        
        # also need to check the converse direction
        # no two letters map to the same word, so make sure that 
        # the values are all unique
        if len(set(bijections.values())) != len(bijections.values()):
            return False


        return True
