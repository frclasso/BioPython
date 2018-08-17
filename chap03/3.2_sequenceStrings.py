#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq=Seq('GATCG', IUPAC.unambiguous_dna)

for index,letter in enumerate(my_seq):
    print("%i %s"%(index, letter))

print('Done.')
