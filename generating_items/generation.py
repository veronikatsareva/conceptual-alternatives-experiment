from random import shuffle, choice, sample

# возможные значения параметров
forms = [
    ["circle", "triangle", "square", "pentagon", "hexagon"],
    ["red", "yellow", "green", "blue", "violet"],
    ["top-left", "top-right", "bottom-left", "bottom-right", "center"],
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
    if strong == "and":
        yes = both[:4]
        no = none[:4]
        if target == "yes":
            quest = both[4]
        elif target == "no":
            quest = none[4]
        else:
            quest = one[0]
    else:
        yes = one[:4]
        no = none[:4]
        if target == "yes":
            quest = one[4]
        elif target == "no":
            quest = none[4]
        else:
            quest = both[0]
    return yes, no, [quest]


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
    if target == "yes":
        quest = true[4]
    else:
        quest = false[4]
    return true[:4], false[:4], [quest]


def generate():
    """
    Функция для генерации всего.
    :returns: список из 20 вопросов. в вопросе 2 кортежа: в первом описывается тест, во втором фигуры.
        описание фигур -- в первом списке 4 кортежа со значениями параметров типа YES, во втором типа NO. кортеж с параметрами вопроса.
    """
    practice = []
    posa1, posa2 = sample([0, 1, 2], 2)
    a1 = choice(forms[posa1])
    yes, no, quest = get_practice(a1, posa1, "yes")
    cur = {"description": (a1, "yes"), "YES": yes, "NO": no, "?": quest}
    practice.append(cur)
    a2 = choice(forms[posa2])
    yes, no, quest = get_practice(a2, posa2, "no")
    cur = {"description": (a2, "no"), "YES": yes, "NO": no, "?": quest}
    practice.append(cur)
    tests = []
    for posa, posb in [(0, 1), (0, 2), (1, 2)]:
        for strong in ["and", "xor"]:
            for target in ["yes", "no", "target"]:
                a = choice(forms[posa])
                b = choice(forms[posb])
                yes, no, quest = get_test(a, posa, b, posb, strong, target)
                cur = {
                    "description": (a, b, strong, target),
                    "YES": yes,
                    "NO": no,
                    "?": quest,
                }
                tests.append(cur)
    shuffle(tests)
    return practice + tests


def make_figure(object, color, place):
    """
    Функция для генерации html-кода для отображения фигуры.
        :param object: вид фигуры
        :param color: цвет фигуры
        :param place: расположение фигуры в сетке 3x3
        :returns: html-строка с кодом
    """
    forms = {
        "object": {
            "circle": "&#9679",
            "triangle": "&#9650",
            "square": "&#9632",
            "pentagon": "&#11039",
            "hexagon": "&#11042",
        },
        "color": {
            "red": "#F60000",
            "yellow": "#FFEE00",
            "green": "#4DE94C",
            "blue": "#3783FF",
            "violet": "#4815AA",
        },
        "place": {
            "top-left": 1,
            "top-right": 3,
            "bottom-left": 7,
            "bottom-right": 9,
            "center": 5,
        },
    }

    template = '<div class="grid-box">\n'

    figure = f'<span style="color: {forms['color'][color]}; font-size: 50px;">{forms['object'][object]}</span>'

    for i in range(1, 10):
        if forms["place"][place] == i:
            template += f'<div class="div{i}">{figure}</div>\n'
        else:
            template += f'<div class="div{i}"></div>\n'

    template += "</div>\n"

    return template


def make_box(figures, question=False, presentation=False):
    """
    Функция для генерации html-кода для отображения контейнера с фигурами.
        :param figures: список фигур, которые будут в контейнере
        :param question: булевый флаг, обозначающий, что создается target или non-target box
        :param presentation: булевый флаг, обозначающий, что создается experiment или presentation box
        :returns: html-строка с кодом
    """
    if not question:
        template = '<div class="box">\n'
    else:
        template = '<div class="question-box">\n'

    for i in range(len(figures)):
        if question and not presentation:
            template += f'<div class="div2">\n'
        else:
            template += f'<div class="div{i + 1}">\n'
        template += make_figure(figures[i][0], figures[i][1], figures[i][2])
        template += "</div>\n"

    template += "</div>"

    return template


def make_html(test):
    """
    Функция для сборки всей html-страницы с заданием эксперимента
        :param test: список фигур для yes-, no-, target-box
        :returns: html-строка с кодом
    """

    template = "<html>\n"
    template += '<link rel="stylesheet" href="global_experiment.css">\n'
    template += "<body>\n"

    # YES-box
    template += "<h2>Каждая из этих фигур удовлетворяет правилу.</h2>\n"
    template += make_box(test["YES"])
    template += "<br>"

    # NO-box
    template += "<h2>Ни одна из этих фигур не удовлетворяет правилу.</h2>\n"
    template += make_box(test["NO"])
    template += "<br>"

    # TARGET-box
    template += "<h2>Эта фигура удовлетворяет правилу?</h2>\n"
    template += make_box(test["?"], question=True)

    template += "</body>\n"
    template += "</html>\n"

    csv = ','.join(test["description"])

    return template, csv

# Генерация тестов и csv с метаданными
tests = generate()
metadata = 'page,feature1,feature2,strong,target\n'

for i in range(len(tests)):
    file_name = f"test{i - 1}"
    if i < 2:
        file_name = f"practice{i + 1}"

    with open(
        f"/Users/veronikatsareva/Desktop/conceptual-alternatives-experiment/chunk_includes/{file_name}.html", "w"
    ) as file:
        template, csv = make_html(tests[i])
        file.write(template)
        if i >= 2:
            metadata += f"{i - 1},{csv}\n"

with open(f"/Users/veronikatsareva/Desktop/conceptual-alternatives-experiment/chunk_includes/metadata.csv", "w") as file:
    file.write(metadata)