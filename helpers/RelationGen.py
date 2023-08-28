from collections import deque
from itertools import islice

def recurrence_relation(seed,func):
    seed = list(seed)
    que = deque(seed,len(seed))
    for x in seed:
        yield seed
    while True:
        out = func(que)
        yield out
        que.append(out)

def note_freqs():
    series = recurrence_relation([55],lambda x: x[-1] * 2**(1 / 12))
    return islice(series, 0, 83)