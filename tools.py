# -*- coding:utf-8 -*-

import cn2an
from openai import OpenAI
from config import llm_model
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8081/v1"



def api_llm(history_list):
    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    chat_response = client.chat.completions.create(
        model=llm_model,
        messages=history_list,
        temperature=0.7,
        top_p=0.8,
        max_tokens=512,
        extra_body={
            "repetition_penalty": 1.05,
        },
    )
    res = chat_response.choices[0].message.content
    return res


def convert_numbers(input_str):
    """将包含数字和中文数字的列表转换为整数列表"""

    if input_str.isdigit():  # 检查是否为数字
        return int(input_str)
    else:
        return cn2an.cn2an(input_str, "normal")




if __name__ == "__main__":
    pass
    # from prompt_temp import history_list2
    # history_list = history_list2
    # a = api_llm(history_list=history_list)
    # print(a)


    # from prompt_temp import history_list1
    # history_list = history_list1
    # a = api_llm(history_list=history_list)
    # print(a)


    from prompt_temp import history_list3
    history_list = history_list3
    a = api_llm(history_list=history_list)
    print(a)

    # # 输入
    # input_list = ["098", "八十七", "七万四千五百五"]
    # # 转换并输出结果
    # for item in input_list:
    #     output = convert_numbers(item)
    #     print(output)


