
reserve = [1, 5, 3]
lost = [6, 2, 4]
n = 6


def solution(n, lost, reserve):
    _reserve = [x for x in reserve if x not in lost]
    _lost = sorted([x for x in lost if x not in reserve])
    print(_lost)
    for i in _reserve:
        if i - 1 in _lost:
            _lost.remove(i - 1)

        elif i + 1 in _lost:
            _lost.remove(i + 1)
    return n - len(_lost)


solution(n, lost, reserve)
