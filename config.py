# path to your own data and coco file
train_data_dir = "data/images"
train_coco = "data/trainval.json"

# Batch size
train_batch_size = 1

# Params for dataloader
train_shuffle_dl = True
num_workers_dl = 4

# Params for training

# Two classes; Only target class or background
num_classes = 2
num_epochs = 10

lr = 0.005
momentum = 0.9
weight_decay = 0.005
