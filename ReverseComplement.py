# -*- coding: utf-8 -*-
"""reversecomplement

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1joQmkwc3fU3tMsP3oMAfnaPFK6qEu1bs
"""

sequence = 'TTGGGGTACTTAATCAGCTTATATAGGTGAAATATCATGCTGTCAGACACGGTCGCGCTTTTGCCACAGGTTGCGGACCTCATGCGGGAACGCTTTGTGCTCCAGTCTTAGGTATACGGTTTCTATCTGACATATTGATTGTGGCCGCCAGCGATTTATCAATTATGATCGGGATGGATTTGGGGGTCTGCGACCAAAACCGCCGCCAGCCGTTCGACTTACCACAGTGGCCTATTACGCGCTGATTACTTTAGGGTGTAGACCACTTTATTTTATCCTAAGTGGCTTCGGATATGTAACGTCCTGCATTTAAAGTGGGGACGCTAAGTATTCACCTTTATCCTGACCTACCTTGCTTATCGCGCGGTGAACCCGAGTATGGAGGATGTCTCTCGTCGTCGATTAGATAAATTATGCGGCCCTAGTTGTCTCCGCCGCGTGTCGTTCACAAGCGCAGCGGGTCTCAAACGTCGTAATTTGAGTCCGCGCGTTCCCTTCGCTCACTTATCAGATTGGAATCCATGCTCTCGGAACCTAGAGGTGGGAGTGGGGATAAATCGTTGTATCTTGTTGGTTTCAGATAGTCGTCACTATCGTAAACTACAGTTGTTAGGCGCGATGAACTCGAAAGTTGGTGGTCCAAACGTCTGAACGTTATGCGGCTACTTCACACATTTTAGAGATGGAATCCCCCAGCGCAATAATAGGGTCCAGATCACACGCCCTCGACCACTTACTCAAGCTAAGAAGACCAATCACTTAGTATAACTGAGTTCTAGGAAGCTTTCCCACACCATGCCTTCCCCACGGTACCGTGAGTTATACTACAGTAGTTCACCAGTGCGAAGCCAATACTTTCAAG'
def revcomplement(seq):
  reverse = seq[::-1]
  print(reverse.replace('A', 'X').replace('T', 'A').replace('X', 'T').replace('G', 'Y').replace('C', 'G').replace('Y', 'C'))
  return

revcomplement(sequence)
