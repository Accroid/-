#!/usr/bin/env python
# coding=gbk

import struct
import hashlib

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def md5(input):
    # �˴���������encode
    # ��д��Ϊhl.update(str)  ����Ϊ�� Unicode-objects must be encoded before hashing
    # input = input.encode('utf-8')
    md5sign = hashlib.md5()
    md5sign.update(input)
    str = md5sign.hexdigest()
    # data = struct.unpack("IIII", str)
    # md5value = data[0] << 96 | data[1] << 64 | data[2] << 32 | data[3]
    return str


# md5value
if __name__ == "__main__":
    str1 = "age=18&mobile=18545878548&name=%E5%BC%A0%E4%B8%89&v_s_k=xinyong234%4021%40%23%24fasd"
    # "mobile=18143488220&sessionToken=1eac3a64ec4e4198867258d044d33e72&v_s_k=xinyong234%4021%40%23%24fasd"

    # string ���ΪList
    strSplit = str1.split('&')  # str.split(str="", num=string.count(str)).
    print (strSplit)
    print ('\n')

    # List����
    strSorted = sorted(strSplit)
    print (strSorted)
    print ('\n')

    # ListתΪstring����&����
    strConvert = '&'.join(strSorted)
    print(strConvert + '\n')

    print (md5(strConvert))
