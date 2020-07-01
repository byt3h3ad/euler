[Problem](https://brilliant.org/daily-problems/non-transitive-dice/)
def win_prob(die1,die2):
    wins = 0
    for a in die1:
        for b in die2:
            if a > b: wins += 1

    return wins/(len(die1)*len(die2))

def wins_from(die, other_dice):
    res = []
    for other_die in other_dice:
        if win_prob(die, other_die) > 0.5:
            res.append(other_die)

    return res

def loses_from(die, other_dice):
    res = []
    for other_die in other_dice:
        if win_prob(die, other_die) < 0.5:
            res.append(other_die)

    return res

given_dice = [[1,1,7,7,7,7], [3,3,3,3,9,9], [5,5,5,5,5,5]]
test_dice = [[0,0,2,2,8,8], [2,2,2,8,8,8], [0,2,8,10,10,10], [0,0,2,2,8,10]]

for die in test_dice:
    print(die," wins from ",len(wins_from(die,given_dice)), "dice")
    print("   and loses from ",len(loses_from(die,given_dice)), "dice")
    print()
