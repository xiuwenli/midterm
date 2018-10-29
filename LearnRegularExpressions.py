#!/usr/bin/python
import fileinput
import re

for line in fileinput.input (['/home/xiuwenli/midterm/Homo_sapiens.GRCh37.75.gtf']):
    geneline = re.findall(r'^([0-9A-Z])\s+', line)
    if geneline:
       print geneline
