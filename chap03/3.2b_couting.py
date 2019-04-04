#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq=Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print(len(my_seq))
print(my_seq.count("G"))

percentage = 100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq)
print(percentage)
print('Done')
