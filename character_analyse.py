# -*- coding:utf-8 -*-
from xiaoshuo_pre import XSSection
from tools import api_llm
from copy import deepcopy


class Character(object):
    pass

    def __init__(self, name):
        pass
        # 人物名称
        self.name = ""
        # 人物介绍
        self.character_setting = ""
        # 自己说过的话
        self.history_chat = [] # (msg, time, to_speeker)

    


class CharacterAnalyse(object):
    pass


    def __init__(self, ):
        pass

        self.characters = ["旁白"]
    
    def format_prompt(self):
        history_chat = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "给我说下为什么刘备要攻打孙权呢"}
        ]
        pass

    @staticmethod
    def text_split_by_len(lines:list):
        """切分到指定附近的长度"""
        # all_lines = "\n".join(lines)
        # print(all_lines)

        p_len = 8  # 每8行是一组
        p = int(len(lines)/p_len)+1
        all_line_group = []
        all_line_index_group = []
        for i in range(p):
            print("--------", i*p_len, "---",(i+1)*p_len)
            if lines[i*p_len:(i+1)*p_len]:
                all_line_group.append(lines[i*p_len: min((i+1)*p_len, len(lines))])
                all_line_index_group.append(list(range(i*p_len, min((i+1)*p_len, len(lines)))))

        return all_line_group, all_line_index_group

    def xs2jvben_first(self, in_xs_section:XSSection):
        """功能：输入一段小说，实现对 role的标记"""
        pass
        from prompt_temp import history_list2

        all_lines_group, all_line_index_group = self.text_split_by_len(in_xs_section.lines)
        role_jvben_list = []

        sun_sec_num = 0
        for item_group in all_lines_group:
            history_list = deepcopy(history_list2)
            this_group_lines = "\n".join(item_group)
            print(this_group_lines)
            print("----+++++")
            history_list[-1]["content"] = history_list[-1]["content"].format(a=this_group_lines).strip()
            print(history_list) 
            print("+++++")
            a = api_llm(history_list=history_list)
            a = "["+a
            a = "kkk第{a}章 第{b}小节 行号:{c}\n".format(a=in_xs_section.index_num, b=sun_sec_num, c=all_line_index_group[sun_sec_num]) + a
            print(a)
            role_jvben_list.append(a)
            sun_sec_num += 1
        
        role_jvben_end = []
        for item_role_jvben in role_jvben_list:
            # 一个子剧本块
            for item_line in item_role_jvben.split("\n"):
                if item_line.strip():
                    role_jvben_end.append(item_line.strip())
        
        print("---本章节文本字数:{a}--句子行数:{b}--切分次数:{c}--剧本行数:{d}".format(
            a=len("\n".join(in_xs_section.lines)), b=len(in_xs_section.lines), c=len(all_lines_group), d=len(role_jvben_end)
            ))
        in_xs_section.role_lines = role_jvben_end

        return in_xs_section

        



    def character_analyse(self):
        """"""
        pass
        # 输入一段xs片段



        # 





if __name__ == "__main__":
    pass




