import os
import codecs
import re

def generate_csv(dir, file):
    # subjects = ['history','pschology','history','sociology','physics','government','economics']
    csv_file = codecs.open(file, 'w+','utf-8')

    for filename in os.listdir(dir):
        with open(os.path.join(dir,filename),encoding='utf-8') as myfile:
            x= myfile.readlines()
            for line in x:
                try:
                    csv_file.write(','.join([re.findall('[a-z]+',filename)[1]]+line.split('\t'))) 
                    #Appending the subject using filename into the row
                except:
                    print('Error: This should have been printed -> '+','.join(line.split('\t')))

    csv_file.close()

path = 'dataset\\'
os.chdir(path)
generate_csv('train_files','train.csv')
generate_csv('dev_files','dev.csv')

