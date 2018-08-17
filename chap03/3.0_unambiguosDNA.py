#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
print(my_seq)
print(my_seq.alphabet)
print("Done.")
