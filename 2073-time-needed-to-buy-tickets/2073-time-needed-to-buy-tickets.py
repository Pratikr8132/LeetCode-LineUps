class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n1 = sum(c if c <= tickets[k] else tickets[k] for c in tickets[:k])
        n2 = sum(c if c <= tickets[k]-1 else tickets[k]-1 for c in tickets[k+1:])
        return n1 + n2 + tickets[k]