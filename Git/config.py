# Model directory
train_dir = "./model"
# Log directory
log_dir   = "./logs"
# Checkpoint
ckpt_name = "conversation.ckpt"

# Data Source
DATA_PATH = "./data/conversation2.txt" # data
VOC_PATH  = "./data/conversation.voc"  # data.voc

# Setting parameters
BATCH_SIZE, EPOCH = 100, 2000
n_hidden, n_layer             = 3, 128
learning_rate, max_decode_len = 0.001, 20

# Special Tokens
PAD,    GO,    EOS,    UNK    = "_PAD_", "_GO_", "_EOS_", "_UNK_"
PAD_ID, GO_ID, EOS_ID, UNK_ID = 0, 1, 2, 3
ALL = [PAD_ID, GO_ID, EOS_ID, UNK_ID]