# -*- coding: utf-8 -*-

"""读取原始文本，将其转换成UTF格式"""
import chardet
from tqdm import tqdm

def text2utf8(in_file, out_file):
    """GB2312格式转UTF-8格式"""
    
    # with open("/home/wangxk/project/product/jvben/data/jvben_source/zhetian.txt", 'rb') as f:
    #     result = chardet.detect(f.read())  # 读取一定量的数据进行编码检测
    # # 打印检测到的编码
    # print("当前输入文件的文件格式是：{a}".format(a=result['encoding']))
    # assert result['encoding'] == "GB2312", u"当前输入文件的文件格式不是GB2312"

    with open(in_file, "r", encoding="GB2312", errors='replace') as in_fp, open(out_file, "w") as out_fp:
        for item_line in tqdm(in_fp):
            # print(item_line)
            # item_line = item_line.decode("gb2312")
            # item_line_utf = item_line.encode("utf-8")
            # print(item_line_utf)
            out_fp.write(item_line)








if __name__ == "__main__":

    in_file = "/home/wangxk/project/product/jvben/data/jvben_source/zhetian.txt"
    out_file = "/home/wangxk/project/product/jvben/data/jvben_source/zhetian_utf.txt"

    text2utf8(in_file, out_file)





