#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

list_of_seqs = [Seq("ACGT", generic_dna), Seq("AACC", generic_dna), Seq("GGTT", generic_dna)]
concatenated = Seq("", generic_dna)
for s in list_of_seqs:
    concatenated += s

print(concatenated)