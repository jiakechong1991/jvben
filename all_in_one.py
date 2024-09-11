# -*- coding:utf-8 -*-
import os, sys
import tqdm
from xiaoshuo_pre import XiaoshuoProcess, XSSection
from character_analyse import CharacterAnalyse
###











##########

# 解析分章节 文本

file_path = "/home/wangxk/project/product/jvben/data/jvben_source/yongsheng.txt"
role_file_path = "/home/wangxk/project/product/jvben/data/jvben_source/yongsheng_role.txt"

###初始化：
if os.path.exists(role_file_path):
    os.remove(role_file_path)


xiaoshuo_ins = XiaoshuoProcess(file_path)
xiaoshuo_ins.split_all_in_one()


character_analyse_ins =  CharacterAnalyse()
# 文本转剧本
for item_index in tqdm.tqdm(xiaoshuo_ins.section_map):
    print("---------当前章节-{a}---------------".format(a=item_index))
    section_ins:XSSection = xiaoshuo_ins.section_map[item_index]
    character_analyse_ins.xs2jvben_first(section_ins)
    section_ins.dump_jvben(role_file_path)

























if __name__ == "__main__":
    pass




