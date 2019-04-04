#!/usr/bin/env python3

from Bio.PDB import *

p=PDBParser()
s=p.get_structure("1fat", "1fat.pdb")
arq = PDBIO()
arq.set_structure(s)
arq.save('out.pbd')