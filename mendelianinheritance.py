# -*- coding: utf-8 -*-
"""mendelianinheritance

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1joQmkwc3fU3tMsP3oMAfnaPFK6qEu1bs
"""

import scipy as scipy
from scipy.special import comb
def probability(k, m, n):
  population_total = k + m + n
  combination_total = comb(population_total, 2)
  valid_combinations = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
  probability = valid_combinations/combination_total
  return probability

probability(17, 25, 19)