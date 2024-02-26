#!/bin/sh env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\s\/images\/smilies\/",line):
        print("hits_to_smilies_directory\t1")
