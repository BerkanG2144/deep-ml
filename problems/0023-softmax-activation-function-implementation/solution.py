import math

def softmax(scores: list[float]) -> list[float]:
    max_score = max(scores)

    exps = []
    for s in scores:
        exps.append(math.exp(s - max_score))

    sum_exps = sum(exps)

    probabilities = []
    for e in exps:
        probabilities.append(e / sum_exps)

    return probabilities