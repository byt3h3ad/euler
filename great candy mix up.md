[Problem](https://brilliant.org/daily-problems/candy-mixed/)
```python
from random import shuffle, choice

bowl = []
sums = {"red": 0, "green": 0}
trials = 1000
cup = 100

for i in range(trials):
    jarA = ["red" for i in range(800)]
    jarB = ["green" for i in range(600)]
    jarB += [jarA.pop() for i in range(cup)]
    shuffle(jarB)
    jarA += [jarB.pop() for i in range(cup)]
    shuffle(jarA)
    bowl += [jarA.pop() for i in range(cup)]
    bowl += [jarB.pop() for i in range(cup)]
    sums[choice(bowl)] += 1

print(round(sums["red"]/trials, 2), round(sums["green"]/trials, 2))
