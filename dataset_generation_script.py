import subprocess
import os
from dataset_creator import generate_csv

def generate_script(task):
    if task == 'subtask1':
        output_path = 'dataset'
        converter = 'task1_converter.py'
    elif task == 'subtask2':
        output_path = 'dataset2'
        converter = 'task2_converter.py'    
    elif task == 'subtask3':
        output_path = 'dataset3'
        converter = 'task3_converter.py'    

    if not output_path in os.listdir('.'):
        os.mkdir(output_path)
    if not 'dev_files' in os.listdir(output_path):
        os.mkdir(os.path.join(output_path,'dev_files'))
        subprocess.call(['python', converter, os.path.join('data','deft_files','dev'), os.path.join(output_path, 'dev_files')])
    else:
        print(f'Dev Dataset for task {task} already exists. Skipping...')
    if not 'train_files' in os.listdir(output_path):        
        os.mkdir(os.path.join(output_path,'train_files'))
        subprocess.call(['python', converter, os.path.join('data','deft_files','train'), os.path.join(output_path, 'train_files')])
    else:
        print(f'Train Dataset for task {task} already exists. Skipping...')

    # subprocess.call(['python','dataset_creator.py'])
    # generate_csv(os.path.join(output_path, 'train_files'),os.path.join(output_path, 'train.csv'))
    # generate_csv(os.path.join(output_path, 'dev_files'),os.path.join(output_path, 'dev.csv'))
    generate_csv(os.path.join(output_path, 'train_files'), converter[:6]+'train.csv')
    generate_csv(os.path.join(output_path, 'dev_files'), converter[:6] +'dev.csv')

generate_script('subtask1')
generate_script('subtask2')
generate_script('subtask3')
