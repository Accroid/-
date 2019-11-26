# _*_ coding:utf-8 _*_
import re

def unicode_to_num(string):
    return "%.1f" %float(string)

def unicode_to_num2(string):
    return "%.1f" %float(string)

def re_num(string):
    p = re.compile(r'\d+\.\d+')
    return "%.2f" %float(p.findall(string)[0])

def remove_string_spaces(string):
    return string.replace(' ', '')

def remove_string_spaces2(string):
    return string.replace('', '')

def remove_unicode_spaces(unicode1):
    return unicode1.replace('\ue68c', '')

def goods_num_split_x(string):
    return int(string.split('x')[1])

def goods_num_split_X(string):
    return int(string.split('×')[1])

def goods_num_split(string):
    return string.split('￥')[1]

def goods_num_split5(string):
    return string.split('￥:')[1]

def goods_num_split2(string):
    return string.split('￥')[0]

def goods_num_split3(string):
    return str(string.split('￥')[0].split('VIP')[0])

def goods_num_split4(string):
    return string.split('￥')[1].replace(' ', '')

def goods_num_split6(string):
    return string.split('万')[0]

def goods_num_split7(string):
    return string.split('¥')[1]

def string_take_num(string):
    p=re.compile(r'\d+')
    return p.findall(string.replace(',',''))[0]