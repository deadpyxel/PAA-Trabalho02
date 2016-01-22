import sys


def gk(i, j):
    return str(i) + ',' + str(j)


def matrix_chain_order(p):
    """
    :param p: array com as dimensões das matrizes
    :return: numero de multiplicações, sequencia de multiplicações
    """
    n = len(p) - 1
    m, s = {}, {}
    for i in range(1, n + 1):
        m[gk(i, i)] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[gk(i, j)] = sys.maxsize
            for k in range(i, j):
                q = m[gk(i, k)] + m[gk(k + 1, j)] + p[i - 1] * p[k] * p[j]
                if q < m[gk(i, j)]:
                    m[gk(i, j)] = q
                    s[gk(i, j)] = k
    return m, s


def get_optimal_parents(s, i, j):
    res = ''
    if i == j:
        return "A" + str(j)
    else:
        res += "("
        res += get_optimal_parents(s, i, s[gk(i, j)])
        res += get_optimal_parents(s, s[gk(i, j)] + 1, j)
        res += ")"
        return res


def mcm_main(p):
    m, s = matrix_chain_order(p)
    total_mult, sequencia = m[gk(1, len(p) - 1)], get_optimal_parents(s, 1, len(p) - 1)
    return total_mult, sequencia
