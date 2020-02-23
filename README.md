# Dataset

This repository contains the raw data and the scripts for the generation of the structured data. To create the dataset, clone the repository and run the following command:

`python dataset_generation_script.py`

# Updating Dataset

To pull new hotness from the public repo:

```
git remote add public https://github.com/adobe-research/deft_corpus
git pull public master
git push origin master
```

Awesome, your private repo now has the latest code from the public repo plus your changes.

# Welcome to the DEFT corpus!

Welcome to the largest expertly annotated corpus for complex definition extraction in free text. Pardon our dust - this data is associated with [SemEval 2020 Task 6](https://competitions.codalab.org/competitions/20900) (DeftEval) and we are releasing the full dataset on the SemEval conference schedule. Train and dev data are available, and test data will become available after the completion of the SemEval evaluation period on 2 Feb 2020. You can source the complete text from the corresponding textbooks at <https://cnx.org>.

The most recent version of the corpus was updated on **16 JAN 2020**.

For more information regarding the annotation, schema, or general characteristics of the corpus, please see our paper [here](https://sigann.github.io/LAW-XIII-2019/pdf/W19-4015.pdf).
  
# Data Format

We are currently releasing annotated data using a CoNLL 2003-like format with the following structure:


    TOKEN TXT_SOURCE_FILE START_CHAR END_CHAR TAG TAG_ID ROOT_ID RELATION

Character indices are derived from the brat standoff format. Tags follow a BIO format with the tag schema outlined in the paper.

# Licensing Information

The entire dataset of textbook sentences with annotations is available for use under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license. Contact the authors for information on commercial use.

# Acknowledgements

We would like to acknowledge the contributions of the annotation team, without which we would not have a corpus to share. Many thanks to Lucino Chiafullo, Danyi Huang, Micaela Kaplan, Roger LaCroix, Molly Moran, Jennifer Pei-Hsuan Lee, Harper Pollio-Barbee, and Keren Sun for their annotations and contributions.

# Citation
If you use the DEFT corpus in your publication, please cite this [paper](https://www.aclweb.org/anthology/W19-4015):

```
@inproceedings{spala-etal-2019-deft,
    title = "{DEFT}: A corpus for definition extraction in free- and semi-structured text",
    author = "Spala, Sasha  and
      Miller, Nicholas A.  and
      Yang, Yiming  and
      Dernoncourt, Franck  and
      Dockhorn, Carl",
    booktitle = "Proceedings of the 13th Linguistic Annotation Workshop",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-4015",
    pages = "124--131",
    abstract = "Definition extraction has been a popular topic in NLP research for well more than a decade, but has been historically limited to well-defined, structured, and narrow conditions. In reality, natural language is messy, and messy data requires both complex solutions and data that reflects that reality. In this paper, we present a robust English corpus and annotation schema that allows us to explore the less straightforward examples of term-definition structures in free and semi-structured text.",
}
```

