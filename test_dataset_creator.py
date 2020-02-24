import os
import codecs
import re
import pandas as pd
import shutil


def subtask_1(dir, file):
    # subjects = ['history','pschology','history','sociology','physics','government','economics']
    # csv_file = codecs.open(file, 'w+','utf-8')
    # csv_file.write(','.join(['Subject','Sentence','Label\n'])) 
    df = pd.DataFrame(columns = ['Subject','Sentence','Label\n'])
    for filename in os.listdir(dir):
        with open(os.path.join(dir,filename),encoding='utf-8') as myfile:
            x= myfile.readlines()
            for line in x:
                try:
                    # csv_file.write(','.join([filename.split('_')[3]]+['"'+line+'"\n'])) 
                    df = df.append({'Subject':filename.split('_')[3], 'Sentence':line.strip()}, ignore_index=True)
                    #Appending the subject using filename into the row
                except Exception as e:
                    print(f'Error: {e} This should have been printed -> '+','.join(line.split('\t')))
    df.to_csv(file, index=False)                
    # csv_file.close()

def submit_subtask1(dir1, dir2, filename,label_col):
    i=0
    test_csv = pd.read_csv(filename)
    y = test_csv[label_col]
    from_dir = dir1
    to_dir = dir2
    # y = [randint(0,1) for i in range(859)]
    # from_dir = os.path.join('data','test_files','subtask_1')
    # to_dir = os.path.join('data','test_files','submit_task_1')
    for file in os.listdir(from_dir):
        to_file = open(os.path.join(to_dir,file),'x',encoding='utf-8') #Creating and writing to a new file
        from_file = open(os.path.join(from_dir,file),'r', encoding='utf-8')
        sentences = from_file.readlines()
        for sentence in sentences:
            to_file.write(sentence.rstrip('\n')+'\t'+str(y[i])+'\n')
            i+=1
        to_file.close()
        from_file.close()

if __name__ == '__main__':
    # Test data for subtask 1
    test_path = os.path.join('data','test_files')

    # To generate test data
    # subtask_1(os.path.join(test_path, 'subtask_1'),'task1_test.csv')

    #To generate submission files
    from_dir = os.path.join('data','test_files','subtask_1')
    to_dir = os.path.join('data','test_files','submit_task_1')
    # if 'submit_task_1' in os.listdir(test_path):
    #     shutil.rmtree(os.path.join(test_path,'submit_task_1'))
    submit_subtask1(from_dir, to_dir, 'submission_baseline.csv','PredictedClass')

