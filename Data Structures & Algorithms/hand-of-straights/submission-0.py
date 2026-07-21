class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        res = []
        sorted_hand = sorted(hand)
        while len(sorted_hand) > 0:
            i = 0
            first = sorted_hand[0]
            for i in range(groupSize):
                next_val = first + i
                if next_val in sorted_hand:
                    sorted_hand.remove(next_val)
                else:
                    return False
        print(sorted_hand)
      
        return True

        