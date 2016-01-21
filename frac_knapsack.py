# retorna o peso agregado a um item
def weight(item):
    return item[1]


# retorna o valor agregado a um item
def value(item):
    return item[2]


# calcula a razão entre valor e peso
def density(item):
    return float(item[2]) / item[1]


def knapsack_greedy(items, max_weight, keyFunc=value):
    """
    :param items: lista de tuplas, onde cada item e da forma ("nome", peso, valor)
    :param max_weight: peso maximo suportado pela mochila
    :param keyFunc: funcao utilizada para sorting, default value
    :returns lista_de_items, peso_total, valor_total
    """

    knapsack = []
    knapsack_peso = 0
    knapsack_valor = 0
    items_sorted = sorted(items, key=keyFunc)
    while len(items_sorted) > 0:
        item = items_sorted.pop()
        if weight(item) + knapsack_peso <= max_weight:
            knapsack.append(item)
            knapsack_peso += weight(item)
            knapsack_valor += value(item)
        else:
            break
    return knapsack, knapsack_peso, knapsack_valor


items = (
    ("mapa", 9, 150), ("bussola", 13, 35), ("agua", 153, 200), ("sanduiche", 50, 160),
    ("glucose", 15, 60), ("lata", 68, 45), ("banana", 27, 60), ("maça", 39, 40),
    ("queijo", 23, 30), ("cerveja", 52, 10), ("protetor solar", 11, 70), ("camera", 32, 30),
    ("camiseta", 24, 15), ("calça", 48, 10), ("guarda chuva", 73, 40),
    ("casaco", 42, 70), ("capa de chuva", 43, 75),
    ("bloco de notas", 25, 80), ("óculos", 7, 20), ("toalha", 18, 12),
    ("meias", 4, 50), ("livro", 30, 10)
)

kn, opt_w, opt_v = knapsack_greedy(items, 300, weight)  # chamada utilizando o peso como funcao de sorting
print("mochila: ", kn, opt_w, opt_v)

kn, opt_w, opt_v = knapsack_greedy(items, 300, value)  # chamada utilizando o valor como funcao de sorting
print("mochila", kn, opt_w, opt_v)

kn, opt_w, opt_v = knapsack_greedy(items, 300, density)  # chamada utilizando a densidade, melhores resultados
print("mochila", kn, opt_w, opt_v)
