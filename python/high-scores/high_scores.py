def latest(scores):
    return scores[-1]


def personal_best(scores):
    
    best = 0

    for score in scores:
        if score > best:
            best = score
    
    return best


def personal_top_three(scores):

    scores = sorted(scores, reverse=True)

    if len(scores) > 3:
        scores = [scores[0], scores[1], scores[2]]
    
    return scores
