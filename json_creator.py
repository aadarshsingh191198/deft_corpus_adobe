import spacy
import networkx as nx
from tqdm import tqdm
import pandas as pd

def jsonify_data(data1, data2, file_name):
    nlp = spacy.load("en_core_web_sm")
    json_dic_list = []
# j=0
    sentence_mismatch=0
    sp_path_error = 0
    for i in tqdm(range(data2.shape[0])):
        doc = nlp(data2['Sentence'][i].strip())
        label =1 

        labels = data2['Label'][i]
        labels = labels.strip().split('  ') #Dunno why a double space is present in the csv
        try:
            assert len(labels) == len(doc)
        except:
            sentence_mismatch+=1


        json_dic = dict()
        tokens, pos, heads, dep_path = [], [], [], []

        for token in doc:
                tokens.append(token.text)
                pos.append(token.pos_)
                heads.append(token.head.i if token.i != token.head.i else -1)
    
        json_dic["tokens"] = tokens
        json_dic["pos"] = pos
        json_dic["heads"] = heads
        json_dic["labels"] = labels
        json_dic["label"] = "definition" if label==1 else "none"

        edges = []
        for token in doc:
                for child in token.children:
                        edges.append(('{0}'.format(child),'{0}'.format(token)))
        graph = nx.Graph(edges)
        
        try:
            entity1 = tokens[labels.index('B-Term')]#.lower()
            entity2 = tokens[labels.index('B-Definition')]#.lower()
        # except:
        #     # print("B-Term or B-Definition not found in ",i)
        #     dep_path = []
        # # print(nx.shortest_path_length(graph, source=entity1, target=entity2))
        # try:
            sp = nx.shortest_path(graph, source=entity1, target=entity2)
            dep_path = [tokens.index(word) for word in sp]

        except:
            sp_path_error+=1
            dep_path = []

        json_dic["dep_path"] = dep_path

        json_dic_list.append(json_dic)

    for i in tqdm(range(data1.shape[0])):
        label == data1['Label'][i]
        if label == 1:
            continue

        doc = nlp(data1['Sentence'][i].strip())
        labels = ['O']*len(doc) 
        try:
            assert len(labels) == len(doc)
        except:
            sentence_mismatch+=1

        json_dic = dict()
        tokens, pos, labels, heads, dep_path = [], [], [], [], []

        for token in doc:
                tokens.append(token.text)
                pos.append(token.pos_)
                heads.append(token.head.i if token.i != token.head.i else -1)

        json_dic["tokens"] = tokens
        json_dic["pos"] = pos
        json_dic["heads"] = heads
        json_dic["labels"] = labels
        json_dic["label"] = "definition" if label==1 else "none"
        
        dep_path = []
        json_dic["dep_path"] = dep_path

        json_dic_list.append(json_dic)

    f = open(file_name,mode= 'w', encoding='utf-8')
    f.write(str(json_dic_list))
    f.close()

    print(f'Sentence mismatch: {sentence_mismatch}, SP path: {sp_path_error}')


if __name__ == '__main__':
    train_task1 = pd.read_csv('task1_train.csv')
    train_task2 = pd.read_csv('task2_train.csv')
    dev_task1 = pd.read_csv('task1_dev.csv')
    dev_task2 = pd.read_csv('task2_dev.csv')

    jsonify_data(train_task1, train_task2, 'train.json')
    jsonify_data(dev_task1, dev_task2, 'dev.json')


