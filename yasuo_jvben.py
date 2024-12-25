# -*- coding:utf-8 -*-
from tools import api_llm
import copy
import tqdm
from xiaoshuo_pre import XiaoshuoProcess, XSSection
from tools import total_token

class YaSuoTool(object):
    pass

    def __init__(self, sections:dict, out_file:str, yasuo_level=1):
        """
        sections: 必须是XiaoshuoProcess.section_map属性
        """
        pass
        self.k = yasuo_level  # 压缩等级
        self.prompt = history_list2 = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": """#你是一个是一个著名小说改编作家，下面是一段小说原文,但是有点冗余，请你对它进行改编批改和删减
###要注意几点：
1. 原文小说很多地方过于繁琐冗余，你要对其进行适当的删减，但是核心情节必须保留，特别是人物关系，还有主角的武器/法术 进化这些关键情节
2. 要保持故事整体连贯，核心情节完整
3. 修改结果要准确，里面【不要包含】修改思路之类话语，因为输出结果【直接作为】【最终结果】给原作者的

###原文如下：
{a}
###请给出精简后的结果："""},
    ]
        self.sections = sections
        self.out_file = out_file
        self.yasuo_before_counter = 0
        self.yasuo_after_counter = 0

    def yasuo_section(self, this_section:str):
        pass
        new_prompt = copy.deepcopy(self.prompt)
        new_prompt[1]["content"] = new_prompt[1]["content"].format(a=this_section)
        out_res =  api_llm(new_prompt)
        self.yasuo_before_counter += len(this_section)
        self.yasuo_after_counter += len(out_res)
        # print("压缩前字数{a}--压缩后字数{b}-".format(a=len(this_section), b=len(out_res)))
        # print("---压缩前-----")
        # print(this_section)
        # print("----压缩后-----")
        # print(out_res)
        # 1/0
        return out_res

    def yasuo(self):
        pass
        # 对section进行 重新分组
        # 文本转剧本
        all_section_lines = []
        all_section_lines_index = [] # 章节序号
        for item_index in tqdm.tqdm(self.sections):
            if item_index >20000000: # 先研究前10章节
                break
            # 获取该章节
            section_ins:XSSection = self.sections[item_index]
            all_section_lines.append("\n".join(section_ins.lines[1:]))  #  这个1是为了去掉 第一行(章节标题行)
            all_section_lines_index.append(item_index)
        print("读取到的章节数量{a}".format(a=len(all_section_lines)))
        print(all_section_lines_index)
        # print(all_section_lines)
        new_section_group = []
        new_section_group_index = []  # 合并章节的起始结束序号
        for index in range(0, len(all_section_lines), self.k):
            pass
            # 左闭右开
            left_index = index
            right_index = (index+self.k) if index+self.k <=(len(all_section_lines_index)-1) else (len(all_section_lines_index)-1)

            new_section_group_index.append([left_index, right_index])
            if left_index == right_index:
                new_section_group.append(all_section_lines[left_index])
            else:
                new_section_group.append("\n".join(all_section_lines[left_index:right_index]))
        print("合并后的章节组个数{a}".format(a=len(new_section_group)))
        print(new_section_group_index)
        # print(new_section_group)
        print("开始执行压缩")
        with open(self.out_file, "a") as fp:
            for item_index in tqdm.tqdm(range(len(new_section_group))):
                item_title = "第{a}章节 ~ 第{b}章节".format(
                    a=new_section_group_index[item_index][0],
                    b=new_section_group_index[item_index][0]
                )
                yasuo_res = self.yasuo_section(new_section_group[item_index])
                print("------当前{e} ：{a}------当前token消耗: {b}(all) = {c}(in) + {d}(out)---压缩比:{f}%---\n".format(
                    a=item_index, b=total_token["total"], c=total_token["in_num"], d=total_token["out_num"],
                    e=item_title, f= round(100*self.yasuo_after_counter/self.yasuo_before_counter, 2)
                ))
                fp.write("{a}\n{b}\n".format(a=item_title, b=yasuo_res))











if __name__ == "__main__":
    pass


