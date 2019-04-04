#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import generic_nucleotide
from Bio.Alphabet import IUPAC

nuc_seq = Seq("GATCGATGC", generic_nucleotide)
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)
print(nuc_seq)
print(dna_seq)
print(nuc_seq + dna_seq)