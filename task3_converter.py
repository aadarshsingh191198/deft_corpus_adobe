from pathlib import Path
import sys
import pandas as pd
import re
import csv

'''
Usage: python3 task1_converter [PATH_TO_SOURCE_DEFT_FILES] [OUTPUT_PATH]

Use this script to convert from the sequence/relation labeling format to classification format.

This produces files in the following tab-delineated format:
[SENTENCE]  [TAGS]

Use this format for SemEval Task 6, subtask 3.

'''

def convert(source_files_path, output_path):
    """
    Walks through the provided source files and finds .deft files to convert
    """
    for child in Path(source_files_path).iterdir():
        if child.suffix == '.deft':
            write_converted(child, Path.joinpath(output_path, child.name))
        elif child.is_dir():
            convert(child, output_path)

def write_converted(source_file, output_file):
    """
    Walks through the conll-type files and converts them to sentence classification format ([SENT]  [BIN_VAL]
    """

    sentences = pd.DataFrame(columns=['sentence', 'relation'])
    with open(source_file, encoding='utf8') as source_text:
        has_def = 0
        new_sentence = ''
        new_relation = ''
        for line in source_text.readlines():

            if re.match('^\s+$', line) and len(new_sentence) > 0 and not re.match(r'^\s*\d+\s*\.$', new_sentence):
                if has_def != 0:
                    sentences = sentences.append({'sentence': new_sentence, 'relation': new_relation}, ignore_index=True)
                new_sentence = ''
                new_relation= ''
                has_def = 0
            if line == '\n':
                continue

            line_parts = line.split('\t')
            new_sentence = new_sentence + ' ' + line_parts[0]
            new_relation = new_relation + ' ' + line_parts[7].rstrip()
            if line_parts[4][3:] == 'Definition':
                has_def = 1
    sentences.to_csv(output_file, header=False, index=False, quoting=csv.QUOTE_ALL, sep='\t')
if __name__ == '__main__':
    convert(Path(sys.argv[1]), Path(sys.argv[2]))