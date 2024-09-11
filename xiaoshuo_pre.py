# -*- coding:utf-8 -*-

import re
import os,sys
from tools import convert_numbers


class XSSection(object):

    @staticmethod
    def format_section_num():
        pass

    pass
    def __init__(self, section_context: str):
        """
        输入：一段文本
        输出：章节序号，章节名称，章节内容
        """
        
        self.index_num:int = -1 # 章节原文上提取到的序号
        self.is_valid = False
        self.section_name:str = ""  # 章节名称
        self.lines:list[str] = []  # 章节的每一行
        self.role_lines:list[str] = []  # 每一行
        self.key_word = []
        last_section_num = -1

        for item in ["(E)，高速全文字在线阅读！"]:
            section_context = section_context.replace(item, "")

        ### 寻找章节title
        # 定义正则表达式模式，匹配“第几章 标题”的格式
        pattern = r"第?[零一二三四五六七八九十百千万0123456789]+章?\s+.+"
        section_text = ""
        section_title = ""
        # 把原文中 的 "章" 临时替换成 "章 "[不改变原文]，是为了方百年 正则表达式进行匹配
        for item_line in section_context.replace("章", "章 ").split("\n"):
            if item_line:
                match = re.search(pattern, item_line)
                if match:
                    section_title = item_line # match.group()
                    break
        
        # 对章节title进行解析 章节序号和章节名称
        if section_title:
            pass
            print("提取到标题行：", section_title)
            self.lines:list[str] = [item_line.strip() for item_line in \
                section_context.replace(section_title, "").split("\n") if item_line.strip()]
            
            # 定义正则表达式模式，匹配“第”开头，后面跟着数字或中文数字，然后是“章”，最后是标题
            pattern = r"第?(\d+|[零一二三四五六七八九十百千万]+)章?\s+(.+)"

            # 遍历文本列表，使用正则表达式搜索并提取章节序号和标题
            match = re.search(pattern, section_title)
            if match:
                try:
                    self.index_num = convert_numbers(match.group(1))
                except Exception as e:
                    self.index_num += 1  # 自动+1，作为它的序号
                    print("序号解析错误， 标题行是：{a}".format(a=section_title))
                last_section_num = self.index_num
                self.section_name = match.group(2)
                print(f"章节序号: {self.index_num}, 标题: {self.section_name}")
                if self.index_num> -1:
                    self.is_valid = True
                    return

            else:
                print("没有找到匹配的章节序号和标题。")
        else:
            print("没有提取到标题行")
        
        if not self.is_valid:
            print("原文如下：")
            print("--{a}--{b}".format(a=section_context[0:100], b=len(section_context)))

        ####常规策略提取不到，下面专注 解析这种问题： 只有章节，没有标题

        # context_line = []
        # title_line = ""
        # for item_line in section_context.split("\n"):
        #     if not item_line.strip():
        #         continue
        #     print(item_line)
        #     pattern = r"第?(\d+|[零一二三四五六七八九十百千万]+)章?\s+"
        #     match = re.search(pattern, item_line)
        #     if match:
        #         section_title = item_line # match.group()
        #         print(match.group())
        #         2/0
        #         break

    def dump_jvben(self, file_path):
        
        all_line = ["第{a}章  {b}".format(a=self.index_num, b=self.section_name)]
        all_line.extend(self.role_lines)
        # if os.path.exists()
        with open(file_path, "a") as fp:
            for item_line in all_line:
                fp.write("{a}\n".format(a=item_line))
        
        



class XiaoshuoProcess(object):
    """实现对小说的各种预处理操作"""
    pass   

    def __init__(self, file_path):
        pass
        self.introduct = ""
        self.file_path = file_path
        self.invalid_flags = []
        self.section_flag= """------------"""
        self.section_map = {} # "index_num": xs_section
    
    def split_all_in_one(self):
        pass
        # 读取文件
        f = open(self.file_path, "r")
        all_lines = "\n".join(f.readlines())
        
        # 根据章节标识符 进行切分
        all_sections = all_lines.split(self.section_flag)
        # 解析章节：提取序号和标题
        max_index = 0
        error_counter = 0
        for item_section in all_sections:
            if not item_section.strip(): # 过滤无效行
                continue
            section_ins_ = XSSection(item_section)
            if section_ins_.is_valid:
                self.section_map[section_ins_.index_num] = section_ins_
                if section_ins_.index_num > max_index:
                    max_index = section_ins_.index_num
            else: # 章节提取失败的，先跳过这个章节吧
                error_counter += 1
                if error_counter>=15:
                    1/0

        print("一共提取出{a}个章节, 作者的最大序号是{b}, 提取失败了{c}个章节， 成功比例:{d}%".format(
            a=len(self.section_map), b=max_index, c=max_index-len(self.section_map),
            d=round(len(self.section_map)/max_index*100, 2)

        ))



if __name__ == "__main__":
    pass
    
#     aa="""


# 第三百零八章 天龙骸骨



#     那二皇子和黄泉魔宗高手“黑幽王”一飞过来，把湖泊上的滚滚乌云全部冲开。



#     同时两大高手双眼放光"""

#     XSSection(aa)

    xiaoshuo_ins = XiaoshuoProcess("/home/wangxk/project/product/jvben/data/jvben_source/yongsheng.txt")
    xiaoshuo_ins.split_all_in_one()







    








if __name__ == "__main__":
    pass






