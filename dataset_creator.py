import os
import codecs
import re

def generate_csv(dir, file):
    # subjects = ['history','pschology','history','sociology','physics','government','economics']
    csv_file = codecs.open(file, 'w+','utf-8')
    csv_file.write(','.join(['Subject','Sentence','Label\n'])) 
    for filename in os.listdir(dir):
        with open(os.path.join(dir,filename),encoding='utf-8') as myfile:
            x= myfile.readlines()
            for line in x:
                try:
                    csv_file.write(','.join([filename.split('_')[3]]+line.split('\t'))) 
                    #Appending the subject using filename into the row
                except:
                    print('Error: This should have been printed -> '+','.join(line.split('\t')))

    csv_file.close()


if __name__ == '__main__':
    # Test data for subtask 1
    test_path = os.path.join('data','test_files')
    generate_csv(os.path.join(test_path, 'subtask_1'),'task1_test.csv')


    # Generate train and dev data for subtasks 

    # path = 'dataset2'
    # task = 'task2_'
    # generate_csv(os.path.join(path, 'train_files'),task+'train.csv')
    # generate_csv(os.path.join(path, 'dev_files'), task+ 'dev.csv')
