from collections import defaultdict


# Classe principal para os nos da arvore Huffman
class Node(object):
    def __init__(self, weight, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right
        self.score = None

    def __str__(self):
        return 'weight:%d,score:%s' % (self.weight, str(self.score))

    def address(self, score, from_parent=None):
        self.score = score
        if from_parent:
            self.score = from_parent + self.score
        if self.left:
            self.left.address('0', self.score)
        if self.right:
            self.right.address('1', self.score)


# classe principal para as folhas da arvore
class Leaf(Node):
    def __init__(self, data, weight):
        self.data = data
        super(Leaf, self).__init__(weight)

    def __str__(self):
        return 'data:%s,' % str(self.data) + super(Leaf, self).__str__()


# geraçao dos codigos de prefixo
def gen_codes(tree):
    char_codes = {}
    if isinstance(tree, Leaf):
        char_codes[tree.data] = tree.score
    if tree.left:
        char_codes.update(gen_codes(tree.left))
    if tree.right:
        char_codes.update(gen_codes(tree.right))
    return char_codes


# funçao principal de encoding
def huffman_encode(inp):
    """
    :param inp: string de dados para encode
    :return: codigos associados, dados encodados
    """
    freqs = defaultdict(int)
    freqs['EOT'] = 0
    for ch in inp: freqs[ch] += 1
    freqs = [Leaf(key, val) for key, val in freqs.items()]
    while len(freqs) > 1:
        freqs = sorted(freqs, key=lambda item: item.weight)
        low1 = freqs.pop(0)
        low2 = freqs.pop(0)
        node = Node(low1.weight + low2.weight, low1, low2)
        freqs.append(node)
    tree = freqs[0]
    tree.address('')
    codes = gen_codes(tree)
    bindata = str()
    for ch in inp:
        bindata += codes[ch]
    bindata += codes['EOT']
    byte_len = 8
    bindata += '0' * (len(bindata) % byte_len)
    index = 0
    encoded = []
    while index < len(bindata):
        encoded.append(int(bindata[index:index + byte_len], 2))
        index += byte_len
    return codes, encoded


def check(pair, word):
    if pair[1] == word:
        return pair


'''
if __name__ == '__main__':
    entrada = \'\'\'
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec congue odio sapien, ac vestibulum lacus euismod vel.
    Quisque semper convallis justo, a porttitor metus dignissim nec. Sed iaculis metus at turpis volutpat, at cursus
    neque gravida. Pellentesque sit amet tortor rhoncus, sagittis justo et, laoreet sem. Duis porttitor blandit mattis.
    Aliquam consequat varius imperdiet. Nullam aliquam id nunc nec egestas.
    \'\'\'

    code, encoded = huffman_encode(entrada)
    print('Tamanho Original:', len(entrada))
    print('Tamanho codificado:', len(encoded))
'''
