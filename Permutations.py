# -*- coding: utf-8 -*-
"""permutations

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XKf46XMa1XWtpl4FfLRNcFSoS60PYQeu
"""

import itertools
n = 6
def permutation(length):
  natural_numbers = [x for x in range(1, length+1)]
  permutations = list(itertools.permutations(natural_numbers))
  print(len(permutations))
  for i in permutations:
    print(str(i).replace('(','').replace(')','').replace(',', ''))
permutation(n)
