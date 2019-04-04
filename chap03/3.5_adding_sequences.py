#!/usr/bin/env python3

from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

protein_seq = Seq("EVRNAK", IUPAC.protein)
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)

#print(protein_seq + dna_seq)
# TypeError: Incompatible alphabets IUPACProtein() and IUPACUnambiguousDNA()

# We have to first give both sequences generic alphabets
from Bio.Alphabet import generic_alphabet
protein_seq.alphabet = generic_alphabet
dna_seq.alphabet = generic_alphabet
print(protein_seq + dna_seq)