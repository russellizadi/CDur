#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import itertools

config_file = "runconfigs/cdur_urban_sed1.yaml"

for rnn, temppool in itertools.product(
    ["GRU", ], # ["GRU", "RNN", "LSTM"] 
    ["linear", ], # ["max", "linear", "attention"]
    ): 
    with open(config_file) as con_read:
        yaml_config = yaml.load(con_read, Loader=yaml.FullLoader)
    print(rnn, temppool)
    yaml_config['model_args']["rnn"] = rnn
    yaml_config['model_args']["temppool"] = temppool
    
    with open(config_file, 'w') as file:
        yaml_config = yaml.dump(yaml_config, file)
    
    command = f"python3 run.py train_evaluate {config_file}  --test_data data_urbansed/features/urban_sed_test.h5 --test_label data_urbansed/flists/urban_sed_test_strong.tsv"
    os.system(command)