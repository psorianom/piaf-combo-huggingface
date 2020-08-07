# PIAFING Around

## Intro

This repo contains the code used to train the models and evaluate French Q&A models trained on French Q&A datasets. This code leverages Hugging Face's off-the-shelf [training scripts](https://github.com/huggingface/transformers/blob/master/examples/question-answering/run_squad.py).

## Preparing the data

We train several models in order to compare them qualitatevly and quantitavely. We employ three datasets : 

1. [PIAFv1.1](https://www.data.gouv.fr/en/datasets/piaf-le-dataset-francophone-de-questions-reponses/)
2. [FQuADv1.0](https://fquad.illuin.tech/)
3. [SQuAD-FR (SQuAD automatically translated to French)](https://github.com/Alikabbadj/French-SQuAD)

A simple process of concatenation is used to join these datasets together (see `./data/squad_joiner.py` for more info). This script takes as input the path of two or more SQuAD-like datasets and outputs a single one with both datasets Q&A pairs.


## Training

Using Hugging Face [script](https://github.com/huggingface/transformers/blob/master/examples/question-answering/run_squad.py) to fine-tune a BERT-like model to solve Q&A, we use the following parameters: 

```
python run_squad.py \
--model_type camembert \
--model_name_or_path camembert-base \
--do_train --do_eval \
--train_file data/SQuAD+fquad+piaf.json \
--predict_file data/fquad_valid.json \
--per_gpu_train_batch_size 12 \ 
--learning_rate 3e-5 \ 
--num_train_epochs 4 \  
--max_seq_length 384 \ 
--doc_stride 128 \
--save_steps 10000 

```

## Usage

The model can be downloaded from Hugging Face hub [here](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf)

## Datasets citations

### PIAF
```
@inproceedings{KeraronLBAMSSS20,
  author    = {Rachel Keraron and
               Guillaume Lancrenon and
               Mathilde Bras and
               Fr{\'{e}}d{\'{e}}ric Allary and
               Gilles Moyse and
               Thomas Scialom and
               Edmundo{-}Pavel Soriano{-}Morales and
               Jacopo Staiano},
  title     = {Project {PIAF:} Building a Native French Question-Answering Dataset},
  booktitle = {{LREC}},
  pages     = {5481--5490},
  publisher = {European Language Resources Association},
  year      = {2020}
}

```

### FQuAD
```
@article{dHoffschmidt2020FQuADFQ,
  title={FQuAD: French Question Answering Dataset},
  author={Martin d'Hoffschmidt and Maxime Vidal and Wacim Belblidia and Tom Brendl'e and Quentin Heinrich},
  journal={ArXiv},
  year={2020},
  volume={abs/2002.06071}
}
```

### SQuAD-FR
```
 @MISC{kabbadj2018,
   author =       "Kabbadj, Ali",
   title =        "Something new in French Text Mining and Information Extraction (Universal Chatbot): Largest Q&A French training dataset (110 000+) ",
   editor =       "linkedin.com",
   month =        "November",
   year =         "2018",
   url =          "\url{https://www.linkedin.com/pulse/something-new-french-text-mining-information-chatbot-largest-kabbadj/}",
   note =         "[Online; posted 11-November-2018]",
 }
 ```
