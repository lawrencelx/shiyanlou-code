#!/usr/local/env python3

import sys

def Hours(min):

    if min < 0:
        raise  ValueError("输入一个自然数字")
    else:
        print(f"{int(min / 60)}小时，{min % 60}分钟")



try:
    Hours(int(sys.argv[1]))
except:
    print("参数错误")
