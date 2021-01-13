def second_highest_score(scores):
    scores.sort(reverse=True)
    maximum = scores[0]
    for score in scores:
        if score < maximum:
            return score


input()
scores = list(map(int, input().split()))
print(second_highest_score(scores))
