from typing import List

"""
Time Complexity: O(n logn + n) = O(n log(n))
Space Complexity (Program): O(n)
Space Complexity (Function): O(1)
"""
def second_highest_score(scores: List[int]):
    # O(n log(n))
    scores.sort(reverse=True)
    maximum = scores[0]
    for score in scores:        # n
        if score < maximum:
            return score


input()
scores = list(map(int, input().split()))
print(second_highest_score(scores))
