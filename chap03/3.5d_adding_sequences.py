#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

list_of_seqs = [Seq("ACGT", generic_dna), Seq("AACC", generic_dna), Seq("GGTT", generic_dna)]
print(sum(list_of_seqs, Seq("", generic_dna)))