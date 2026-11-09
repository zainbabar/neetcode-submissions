class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        for bill in bills:
            # no change needed
            if bill == 5:
                fives += 1
            elif bill == 10:
                # have a five to give back as change
                if fives > 0:
                    fives -= 1
                    tens += 1
                # dont have a five cant give change fails
                else:
                    return False
            elif bill == 20:
                # either give back a ten and a five or 3 fives
                # want to get rid of tens first b/c only twenties can get tens
                # as change. fives are last resort 
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                    twenties += 1
                elif fives >= 3:
                    fives -= 3
                    twenties += 1
                else:
                    return False

        return True
