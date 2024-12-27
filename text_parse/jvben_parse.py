# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import os, sys
import tqdm
from text_parse.split_section import XiaoshuoProcess, XSSection
from character_analyse import CharacterAnalyse
from config import total_token

"""
本程序 实现如下功能：
1. 读取一本小说
2. 按照章节解析：章节号，章节名，章节内容
3. 输出是一个格式化好的 json结构
"""

def JvbenParse(file_path):
    """
    in: file_path : 输入文件的 路径
    out:  xiaoshuo_map : 解析后的 章节
    {
        3: {
            "title": "xxx",
            "content": []
        }
    }
    """

    # 切分章节
    xiaoshuo_ins = XiaoshuoProcess(file_path)
    xiaoshuo_ins.split_all_in_one()
    xiaoshuo_map  = dict()

    for item_section_index, item_sction in xiaoshuo_ins.section_map.items():
        xiaoshuo_map[item_section_index] = {
            "title": item_sction.section_name,
            "content": item_sction.dump_jvben()
        }
    return xiaoshuo_map




if __name__ == "__main__":
    pass










