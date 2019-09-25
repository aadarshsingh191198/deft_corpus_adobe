import subprocess
import os

os.mkdir('dataset')
os.mkdir(os.path.join('dataset','dev_files'))
os.mkdir(os.path.join('dataset','train_files'))

subprocess.call(['python','task1_converter.py',os.path.join('data','deft_files','dev'),os.path.join('dataset','dev_files')])
subprocess.call(['python','task1_converter.py',os.path.join('data','deft_files','train'),os.path.join('dataset','train_files')])

subprocess.call(['python','dataset_creator.py'])

