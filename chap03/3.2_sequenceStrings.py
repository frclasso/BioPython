#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq=Seq('GATCG', IUPAC.unambiguous_dna)

for index,letter in enumerate(my_seq):
    print("%i %s"%(index, letter))

print()
print('Tamanho:',len(my_seq))
print()
print(my_seq[0])
print(my_seq[1])
print(my_seq[2])

print('Done.')
