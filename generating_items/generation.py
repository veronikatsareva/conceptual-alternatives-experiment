from random import shuffle, choice, sample

# возможные значения параметров
forms = [
    ['circle', 'triangle', 'square', 'pentagon', 'hexagon'],
    ['red', 'yellow', 'green', 'blue', 'violet'],
    ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'center']
]

# все фигуры
coords = [(x, y, z) for x in forms[0] for y in forms[1] for z in forms[2]]

def group(a, posa, b, posb):
    """
    Функция для разбиения фигур на группы относительно двух зафиксированных параметров.
    :param a: значение первого параметра
    :param posa: тип параметра от 0 до 2
    :param b: значение второго параметра
    :param posb: тип параметра от 0 до 2
    :returns: три списка. в первом оба параметра совпадают с целевыми, во втором ровно один, в третьем ни одного.
    """
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
    """
    Функция для генерации одного теста.
    :param a: значение первого параметра
    :param posa: тип параметра от 0 до 2
    :param b: значение второго параметра
    :param posb: тип параметра от 0 до 2
    :param strong: вторая операция из пары (and / xor)
    :param target: тип фигуры в вопросе (yes / no / target)
    :returns: в первом списке 4 кортежа со значениями параметров типа YES, во втором типа NO. кортеж с параметрами вопроса.
    """
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
    """
    Функция для генерации тренировки.
    :param a: значение параметра
    :param posa: тип параметра от 0 до 2
    :param target: тип фигуры в вопросе (yes / no)
    :returns: в первом списке 4 кортежа со значениями параметров типа YES, во втором типа NO. кортеж с параметрами вопроса.
    """
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
    """
    Функция для генерации всего.
    :returns: список из 20 вопросов. в вопросе 2 кортежа: в первом описывается тест, во втором фигуры.
        описание фигур -- в первом списке 4 кортежа со значениями параметров типа YES, во втором типа NO. кортеж с параметрами вопроса.
    """
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