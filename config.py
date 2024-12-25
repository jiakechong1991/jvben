# -*- coding:utf-8 -*-

import os, sys

HOME_FOLDER= os.path.dirname(os.path.realpath(__file__))
sys.path.append(HOME_FOLDER)


model_config = {
    "qwen2.5-1.5B": {
        "llm_path": "/home/wangxk/project/model_bin_common/Qwen2.5-1.5B-Instruct",
        "url": "http://10.58.68.15:8083/v1"
    },
    "qwen2.5-3B": {
        "llm_path": "/home/wangxk/project/model_bin_common/Qwen2.5-3B-Instruct",
        "url": "http://10.58.68.15:8081/v1"
    },
    "qwen2.5-7B": {
        "llm_path": "/home/wangxk/project/model_bin_common/Qwen2.5-7B-Instruct",
        "url": "http://10.58.68.15:8082/v1"
    }
}


total_token = {
    "total": 0,
    "in_num": 0,
    "out_num": 0
}





