#!/usr/bin/python

from Bio import SeqIO

records = list(SeqIO.parse("ls_orchid.gbk", "genbank"))

print("")
print("Found %i records" % len(records))
print("")

print("***********************************************************************")
print("The last record\n")
last_record = records[-1]
print("ID: {}".format(last_record.id))
print(repr(last_record.seq))
print("Tamanho:  {}".format (len(last_record)))

print("************************************************************************")
print("First record\n")
first_record = records[0]
print("ID: {}".format(first_record.id))
print(repr(first_record.seq))
print("Tamanho:  {}".format (len(first_record)))

