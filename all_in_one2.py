# -*- coding:utf-8 -*-
import os, sys
import tqdm
from xiaoshuo_pre import XiaoshuoProcess, XSSection
from character_analyse import CharacterAnalyse
from config import total_token
from yasuo_jvben import YaSuoTool
###


##########

# 解析分章节 文本

file_path = "/home/wangxk/project/product/jvben/data/jvben_source/yongsheng.txt"
yasuo_file_path = "/home/wangxk/project/product/jvben/data/out/yongsheng_yasuo.txt"

###初始化：
if os.path.exists(yasuo_file_path):
    os.remove(yasuo_file_path)

# 切分章节
xiaoshuo_ins = XiaoshuoProcess(file_path)
xiaoshuo_ins.split_all_in_one()


character_analyse_ins =  CharacterAnalyse()
# 文本转剧本
print("@@@开始进行的role提取工作")
yasuo_ins = YaSuoTool(sections=xiaoshuo_ins.section_map, out_file=yasuo_file_path, yasuo_level=1)
yasuo_ins.yasuo()

























if __name__ == "__main__":
    pass




