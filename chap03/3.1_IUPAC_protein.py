#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_prot=Seq("AGTACACTGGT", IUPAC.protein)
print(my_prot)
print(my_prot.alphabet)
print('Done.')
