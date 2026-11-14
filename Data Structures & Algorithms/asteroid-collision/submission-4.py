class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # add new asteroid if stack is empty
        # if stack has smth and new asteroid cause collision 
        # keep casuing collisions
        stack = []
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue

            cur_asteroid = asteroids[i]
            prev_asteroid = stack[-1]
            # while there is a sign diff keep destroying
            if prev_asteroid > 0 and cur_asteroid < 0:
                same = False
                while prev_asteroid > 0 and cur_asteroid < 0:
                    # both asteroids got destroyed so go onto the next iteration
                    if abs(prev_asteroid) == abs(cur_asteroid):
                        same = True
                        stack.pop()
                        break
                    else:
                        if abs(prev_asteroid) > abs(cur_asteroid):
                            survivor = prev_asteroid
                        else:
                            survivor = cur_asteroid
                        
                        # get rid of the asteroid t hat exploded and update our prev asteroid
                        stack.pop()
                        # no more asteroids
                        if not stack:
                            cur_asteroid = survivor
                            break
                        # still exist more asteroids so repeat this loop thing
                        prev_asteroid = stack[-1]
                        cur_asteroid = survivor

                if not same:
                    stack.append(cur_asteroid)

            else:
                stack.append(cur_asteroid)

        return stack

        # stack = []
        # for i in range(len(asteroids)):
        #     # no asteroids in the stack yet
        #     if not stack:
        #         stack.append(asteroids[i])
        #         continue
            
        #     cur_asteroid = asteroids[i]
        #     prev_asteroid = stack[-1]
        #     # asteroids are moving two diff directions so one will be destroyed
        #     if prev_asteroid < 0 and cur_asteroid > 0 or prev_asteroid > 0 and cur_asteroid < 0:
        #         # same weight both explode so pop whatever on the stack and then move on 
        #         if abs(prev_asteroid) == abs(cur_asteroid):
        #             stack.pop()
        #         else:
        #             survivor = max(abs(prev_asteroid), abs(cur_asteroid))
        #             if survivor == abs(prev_asteroid):
        #                 survivor = prev_asteroid
        #             else:
        #                 survivor = cur_asteroid

        #             stack.pop()
        #             stack.append(survivor)
        #     # was moving in same dir, so js add to stack
        #     else:
        #         stack.append(cur_asteroid)
        
        # return stack

