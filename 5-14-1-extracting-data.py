#!/usr/bin/python
import Bio
from Bio import SeqIO

print("")
record_iterator = SeqIO.parse("ls_orchid.gbk", "genbank")
first_record = next(record_iterator)
print(first_record)
print('')
print("Annotations: {}".format(first_record.annotations))
print('')
print("Annotations Values: {}".format(first_record.annotations.values()))
print('')
print("Annotations Keys: {}".format(first_record.annotations.keys()))
print('')
print("Source: {}".format(first_record.annotations["source"]))
print('')
print("Organism: {}".format(first_record.annotations["organism"]))