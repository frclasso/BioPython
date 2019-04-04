#!/usr/bin/env python3

# slicing sequence
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPAC.unambiguous_dna)
print(my_seq[4:12])
print(my_seq[0::3]) # pula de 3 em 3
print(my_seq[1::3]) # começa no segundo elemento e pula de 3 em 3
print(my_seq[2::3]) # começa no terceiro elemento e pula de 3 em 3
print(my_seq[::-1]) # inverte a sequencia
print(type(my_seq))
my_seq = str(my_seq)
print(type(my_seq))
print(my_seq)