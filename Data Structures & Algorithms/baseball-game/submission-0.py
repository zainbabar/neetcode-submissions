class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # use a stack here so we can know what the most recent score added is
        scores = []
        for index, op in enumerate(operations):
            if op == "+":
                new_score = scores[-1] + scores[-2]
                scores.append(new_score)
            elif op == "D":
                scores.append((scores[-1] * 2))
            elif op == "C":
                scores.pop()
            # plain integer case, just add it 
            else:
                scores.append(int(op))
        return sum(scores)