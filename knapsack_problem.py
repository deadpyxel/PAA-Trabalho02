# noinspection PyBroadException
try:
    xrange
except:
    xrange = range


def totalvalue(comb):
    # Totaliza uma colecao de items
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)


def knapsack01(items, limit):
    """
    :param items: lista de items
    :param limit: peso mácimo suportado
    :return: lista com itens escolhidos
    """
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j - 1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result


items = (
    ("mapa", 9, 150), ("bussola", 13, 35), ("agua", 153, 200), ("sanduiche", 50, 160),
    ("glucose", 15, 60), ("lata", 68, 45), ("banana", 27, 60), ("maça", 39, 40),
    ("queijo", 23, 30), ("cerveja", 52, 10), ("protetor solar", 11, 70), ("camera", 32, 30),
    ("camiseta", 24, 15), ("calça", 48, 10), ("guarda chuva", 73, 40),
    ("casaco", 42, 70), ("capa de chuva", 43, 75),
    ("bloco de notas", 25, 80), ("óculos", 7, 20), ("toalha", 18, 12),
    ("meias", 4, 50), ("livro", 30, 10)
)

bagged = knapsack01(items, 300)
print("Os seguintes items foram empacotados: \n  " +
      '\n  '.join(sorted(item for item, _, _ in bagged)))
val, wt = totalvalue(bagged)
print("Valor Total: [%i] | Peso Total: [%i]" % (val, -wt))
