#!/usr/bin/python

import Bio
from Bio import SeqIO

all_species = []
for seq_record in SeqIO.parse('ls_orchid.gbk', 'genbank'):
    all_species.append(seq_record.annotations["organism"])
print(all_species)