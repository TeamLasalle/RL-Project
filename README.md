# RL-Project - RL Chatbot

## generate response by pre-trained model

__Seq2Seq generate response__
```bash
./script/run.sh S2S /output/test.txt /output/S2S_Response.txt
```
__Reinforcement Learning generate response__
```bash
./script/run.sh RL /output/test.txt /output/RL_Response.txt__
```
\<TYPE\> can be one of below:
1. S2S
2. RL

\<INPUT FILE\> is the testing data

you can just use *tmp/sample_input.txt* or *tmp/sample_input_new.txt* in this repository for convenience

or you can create your own testing data (copy the format from abovementioned files)

\<OUTPUT FILE\> is the output of input file

type any filename you want

## simulate a dialogue by pre-trained model

__Seq2Seq 1 simulate dialog__
```bash
./script/simulate.sh model/Seq2Seq/model-77 1 /output/test.txt /output/S2S_1_Dialog.txt__
```
__Seq2Seq 2 simulate dialog__
```bash
./script/simulate.sh model/Seq2Seq/model-77 2 /output/test.txt /output/S2S_2_Dialog.txt__
```
__Reinforcement Learning 1 simulate dialog__
```bash
./script/simulate.sh model/RL/model-56-3000 1 /output/test.txt /output/RL_1_Dialog.txt__
```
__Reinforcement Learning 2 simulate dialog__
```bash
./script/simulate.sh model/RL/model-56-3000 2 /output/test.txt /output/RL_2_Dialog.txt__
```
for \<PATH TO MODEL\>

to generate seq2seq dialog, type model/Seq2Seq/model-77

to generate RL dialog, type model/RL/model-56-3000

\<SIMULATE TYPE\> can be 1 or 2

the number represents # of former sentence(s) that chatbot considers

__if you choose 1, chatbot only considers user's utterance__

__if you choose 2, chatbot will considers user's utterance and chatbot's last utterance__

\<INPUT FILE\> is the testing data

you can just use *tmp/sample_input.txt* or *tmp/sample_input_new.txt* in this repository for convenience

or you can create your own testing data (copy the format from abovementioned files)

\<OUTPUT FILE\> is the output of input file

type any filename you want

## start training
### Step0: change configs
###### the training config is located in *python/config.py*

you can change some training hyper-parameters, or just keep the original one

### Step1: download data & libraries
we use [Cornell Movie-Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)

you need to download it and put it into data/ directory

and you need to download some libraries with pip:
```bash
pip install -r requirements.txt
```

### Step2: parse data
```bash
./script/parse.sh
```

### Step3: train a Seq2Seq model
```bash
./script/train.sh
```

### Step4-1: test a Seq2Seq model
```bash
./script/test.sh <PATH TO MODEL> <INPUT FILE> <OUTPUT FILE>
```

### Step4-2: simulate a dialog
```bash
./script/simulate.sh <PATH TO MODEL> <SIMULATE TYPE> <INPUT FILE> <OUTPUT FILE>
```
\<SIMULATE TYPE\> can be 1 or 2

the number represents # of former sentence(s) that chatbot considers

if you choose 1, chatbot will only considers user's utterance

if you choose 2, chatbot will considers user's utterance and chatbot's last utterance

### Step5: train a RL model
you can change the training_type parameter in *python/config.py*

'normal' for seq2seq training, 'pg' for policy gradient

you need to first train with 'normal' for some epochs till stable (at least 30 epoches is highly recommended)

then change the method to 'pg' to optimize the reward function

```bash
./script/train_RL.sh
```

*When training with policy gradient*

*you may need a reversed model*

*you can train it by your-self*

*or you can download pre-trained reversed model by*
```bash
./script/download_reversed.sh
```
*the reversed model is also trained by cornell movie-dialogs dataset, but with source and target reversed.*

*you don't need to change any setting about reversed model if you use pre-trained reversed model*

### Step6-1: test a RL model
```bash
./script/test_RL.sh <PATH TO MODEL> <INPUT FILE> <OUTPUT FILE>
```

### Step6-2: simulate a dialog
```bash
./script/simulate.sh <PATH TO MODEL> <SIMULATE TYPE> <INPUT FILE> <OUTPUT FILE>
```
\<SIMULATE TYPE\> can be 1 or 2

the number represents # of former sentence(s) that chatbot considers

if you choose 1, chatbot will only considers user's utterance

if you choose 2, chatbot will considers user's utterance and chatbot's last utterance
