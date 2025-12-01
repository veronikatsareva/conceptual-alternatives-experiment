from random import shuffle, choice, sample

forms = [
    ['circle', 'triangle', 'square', 'pentagon', 'hexagon'],
    ['red', 'yellow', 'green', 'blue', 'violet'],
    ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'center']
]

coords = [(x, y, z) for x in forms[0] for y in forms[1] for z in forms[2]]

def group(a, posa, b, posb):
    both, one, none = [], [], []
    for c in coords:
        if c[posa] == a and c[posb] == b:
            both.append(c)
        elif c[posa] == a or c[posb] == b:
            one.append(c)
        else:
            none.append(c)
    return both, one, none

def get_test(a, posa, b, posb, strong, target):
    both, one, none = group(a, posa, b, posb)
    shuffle(both)
    shuffle(one)
    shuffle(none)
    if strong == 'and':
        yes = both[:4]
        no = none[:4]
        if target == 'yes':
            quest = both[4]
        elif target == 'no':
            quest = none[4]
        else:
            quest = one[0]
    else:
        yes = one[:4]
        no = none[:4]
        if target == 'yes':
            quest = one[4]
        elif target == 'no':
            quest = none[4]
        else:
            quest = both[0]
    return yes, no, quest

def get_practice(a, posa, target):
    true = [c for c in coords if c[posa] == a]
    false = [c for c in coords if c[posa] != a]
    shuffle(true)
    shuffle(false)
    if target == 'yes':
        quest = true[4]
    else:
        quest = false[4]
    return true[:4], false[:4], quest

def generate():
    practice = []
    posa1, posa2 = sample([0, 1, 2], 2)
    a1 = choice(forms[posa1])
    a2 = choice(forms[posa2])
    practice.append(((a1, 'yes'), get_practice(a1, posa1, 'yes')))
    practice.append(((a2, 'no'), get_practice(a2, posa2, 'no')))
    tests = []
    for posa, posb in [(0, 1), (0, 2), (1, 2)]:
        for strong in ['and', 'xor']:
            for target in ['yes', 'no', 'target']:
                a = choice(forms[posa])
                b = choice(forms[posb])
                tests.append(((a, b, strong, target), get_test(a, posa, b, posb, strong, target)))
    shuffle(tests)
    return practice + tests