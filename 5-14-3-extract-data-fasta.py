#!/usr/bin/python

import Bio
from Bio import SeqIO

all_species  = []
for seq_record in SeqIO.parse('ls_orchid.fasta', 'fasta'):
    all_species.append(seq_record.description.split()[1])
print(all_species)
