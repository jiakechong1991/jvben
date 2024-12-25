# -*- coding:utf-8 -*-
import os, sys
import tqdm
from xiaoshuo_pre import XiaoshuoProcess, XSSection
from character_analyse import CharacterAnalyse
from config import total_token
###











##########

# 解析分章节 文本

file_path = "/home/wangxk/project/product/jvben/data/jvben_source/yongsheng.txt"
role_file_path = "/home/wangxk/project/product/jvben/data/out/yongsheng_role.txt"

###初始化：
if os.path.exists(role_file_path):
    os.remove(role_file_path)

# 切分章节
xiaoshuo_ins = XiaoshuoProcess(file_path)
xiaoshuo_ins.split_all_in_one()


character_analyse_ins =  CharacterAnalyse()
# 文本转剧本
print("@@@开始进行的role提取工作")
for item_index in tqdm.tqdm(xiaoshuo_ins.section_map):
    if item_index >2: # 先研究前10章节
        break
    print("---------当前章节号：{a}------当前token消耗: {b}(all) = {c}(in) + {d}(out)---------\n".format(
        a=item_index, b=total_token["total"], c=total_token["in_num"], d=total_token["out_num"]
    ))
    section_ins:XSSection = xiaoshuo_ins.section_map[item_index]
    # print("\n".join(section_ins.lines))
    # 分析章节
    character_analyse_ins.xs2jvben_first(section_ins)
    section_ins.dump_jvben(role_file_path)

























if __name__ == "__main__":
    pass




