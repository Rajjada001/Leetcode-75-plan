class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0,len(tokens)-1
        score = 0
        max_score = 0
        while l<=r:
            # red_power = 0
            if power >= tokens[l]:
                power = power-tokens[l]
                score += 1
                max_score = max(score, max_score)
                l+=1
            elif  score > 0:
                power += tokens[r]
                score -= 1
                r-=1
            # l += 1
            # r-=1
            else:
                break
        return max_score
