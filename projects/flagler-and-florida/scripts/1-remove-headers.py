from pathlib import Path
import os

## The original text files are deliniated by the following header
#
# ## p. 170 (#182) ############################################
# 
# This script removes the header and saves the file to a new directory.

os.makedirs('../working/text', exist_ok=True)

text_files = Path('../original/text').glob('*.txt')

for i in text_files:
    filename = f"../working/text/{i.stem}.working.txt"

    with open(i, 'r', encoding="utf8") as infile, open(filename, 'w', encoding="utf8") as outfile:
        data = infile.read()
        data = data.split('########\n', 1)[1]
        outfile.write(data)