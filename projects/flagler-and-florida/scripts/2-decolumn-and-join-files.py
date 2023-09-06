from pathlib import Path
import os

# os.makedirs('../editing/cleaned', exist_ok=True)
text_files = Path('../editing/text').glob('*.txt')
filename = f"../editing/phase_1.txt"

all_pages = ''

for i in text_files:

    with open(i, 'r', encoding="utf8") as infile:
        col_1 = []
        col_2 = []

        for line in infile:
            col_1.append(line[:48] + "\n")
            col_2.append(line[48:])

        both_cols = col_1 + col_2

    # any line starting with 4 spaces turn into a new line
    for i, line in enumerate(both_cols):
        if line.startswith("    "):
            both_cols[i] = "<newline>" + line[4:]

    page_str = ' '.join(both_cols)

    # find 2 '\n' and replace with <newline>
    page_str = page_str.replace("\n\n", "<newline>")

    # remove all line breaks '\n'
    page_str = page_str.replace("\n", "")

    # replace multiple spaces with a single space
    page_str = ' '.join(page_str.split())

    # add page to all pages
    all_pages  += f"<newpage>" + page_str 


all_pages = all_pages.replace("<newline>", "\n\n")
all_pages = all_pages.replace("<newpage>", "")

with (open(filename, 'w', encoding="utf8")) as outfile:
    outfile.write(all_pages)