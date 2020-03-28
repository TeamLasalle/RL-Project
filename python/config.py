# path to training data
training_data_path = './data/conversations_lenmax22_formersents2_with_former'

# path to all_words
all_words_path = './data/all_words.txt'

# training parameters 
CHECKPOINT = True
train_model_path = './model/RL'
train_model_name = 'model-56-3000'
start_epoch = 30
start_batch = 0
batch_size = 10

# for RL training
training_type = 'pg' # 'normal' for seq2seq training, 'pg' for policy gradient
reversed_model_path = './model/Reversed'
reversed_model_name = 'model-63'

# data reader shuffle index list
load_list = False
index_list_file = './data/shuffle_index_list'
cur_train_index = start_batch * batch_size

# word count threshold
WC_threshold = 20
reversed_WC_threshold = 6

# dialog simulation turns
MAX_TURNS = 10
