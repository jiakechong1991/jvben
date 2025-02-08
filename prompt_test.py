# -*- coding:utf-8 -*-

from openai import OpenAI
from config import model_config, total_token

openai_api_key = "EMPTY"
modle_ins = "qwen2.5-1.5B"
#model=model_config["qwen2.5-3B"],
#model=model_config["qwen2.5-7B"],

def api_llm(history_list):
    client = OpenAI(
        api_key=openai_api_key,
        base_url=model_config[modle_ins]["url"]
    )

    chat_response = client.chat.completions.create(
        model=model_config[modle_ins]["llm_path"],
        messages=history_list,
        temperature=0.7,
        top_p=0.8,
        max_tokens=10000,
        extra_body={
            "repetition_penalty": 1.05,
        },
    )

    print("本次token消耗: {a}".format(a=chat_response.usage.total_tokens))
    total_token["total"] += chat_response.usage.total_tokens
    total_token["in_num"] += chat_response.usage.prompt_tokens
    total_token["out_num"] += chat_response.usage.completion_tokens

    res = chat_response.choices[0].message.content
    return res




"""
方寒体内蓄积已久的“木皇真气”终在与水蛊天魔十万魔兵的激战后，于凝练道家罡气的关键时刻遭遇重创，延缓了进阶的步伐。他曾因世界之树碎片的滋养，将木皇真气锤炼至炉火纯青，为日后修行奠定了坚实基础。若非此碎片，他虽能速成罡气，根基却难稳固，恐需滞留于罡气境数十年，且威力有限。
如今，尽管罡气凝练之路曲折，但根基之深，法力之广，实乃惊人。尤其在吞服“法圣舍利”后，实力更是远超普通仙道弟子，非同寻常。法力，乃个人本命元气，愈强则灵魂愈盛。历经重重磨砺，方寒的真气终在七叶魔君的重压下，水到渠成，化真为罡。
罡气之质，远胜真气，威力无匹，精神与法力随之飞跃，犹如官场品级之跃升，神通之境亦然。方寒今有万马之力，纵使面对八万天魔与绝品宝器，亦能从容应对，皆因境界之差。
脑内真气结晶、融解，化为液态木纹罡气，方寒顿感蜕变，欣喜若狂。“你竟在此时炼气成罡，步入元罡境！”阎惊叹方寒之变，似蝶破茧，气势如参天巨木，傲立风雨。青帝木皇功，神通绝顶，每进一境，潜力无穷。
方寒怒吼：“天地真罡，聚我身，土木相生，五行合一！”真气运转骤增，全面蜕变，融汇为罡。阎罗金身更显柔韧，骨软如棉，筋硬似钢，血气涌动，精神升华，法力与罡气共鸣。体内金色颗粒，九窍金丹残余药力，升腾转化，黄泉大帝遗宝之妙，远超想象。
脑中神秘穴窍逐一洞开，潜力释放，磅礴罡气涤荡全身，毛孔喷射刀剑般罡风，威力惊人。方寒一运功，毛孔罡风竟堪比强弓劲弩，这般力量，恐令天人境高手亦震撼。
轰鸣声中，所有真气终化为木皇罡气，方寒力量倍增，达三万之巨，根基之厚，法力之强，令人咋舌。伤势痊愈，龙腾虎跃，全盛之态。他狂笑道：“天不绝我，压力之下，突破在即，若非此番挑战，恐需苦修多时。七叶魔君，困我不易矣！”
罡气爆发，涌入王鼎大阵，尤以“大力魔神阵”最为壮观。方寒驱动之下，王鼎黑气滚滚，化为巨大魔神，心脏处正是王鼎本身，宛如小山。魔神咆哮，魔掌一拍，七叶魔君的“金蛇斗罗阵”瞬息瓦解。
"""


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
    history_list3 = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": """凡人修仙传 这个小说的男主叫做韩立，你知道这个小说的作者是谁吗？"""},
    ]

    history_list = history_list3
    a = api_llm(history_list=history_list)
    print(a)

    # # 输入
    # input_list = ["098", "八十七", "七万四千五百五"]
    # # 转换并输出结果
    # for item in input_list:
    #     output = convert_numbers(item)
    #     print(output)


