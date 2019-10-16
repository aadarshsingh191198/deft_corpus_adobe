import subprocess
import os

os.mkdir('dataset2')
os.mkdir(os.path.join('dataset2','dev_files'))
os.mkdir(os.path.join('dataset2','train_files'))

subprocess.call(['python','task2_converter.py',os.path.join('data','deft_files','dev'),os.path.join('dataset2','dev_files')])
subprocess.call(['python','task2_converter.py',os.path.join('data','deft_files','train'),os.path.join('dataset2','train_files')])

subprocess.call(['python','dataset2_creator.py'])