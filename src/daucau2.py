#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
# Lê Quốc Tuấn <mr.lequoctuan@gmail.com>, 2014.
# Trần Ngọc Quân <vnwildman@gmail.com>, 2014-2015.

import re
from sys import argv

MAPS = {
    'uỳ': 'ùy',
    'uý': 'úy',
    'uỷ': 'ủy',
    'uỹ': 'ũy',
    'uỵ': 'ụy',
    'oà': 'òa',
    'oá': 'óa',
    'oả': 'ỏa',
    'oã': 'õa',
    'oạ': 'ọa',
    'oè': 'òe',
    'oé': 'óe',
    'oẻ': 'ỏe',
    'oẽ': 'õe',
    'oẹ': 'ọe'
}
maps1 = {k.upper(): v.upper() for k, v in MAPS.items()}
maps2 = {k.capitalize(): v.capitalize() for k, v in MAPS.items()}
maps3 = {k[0]+k[1].upper(): v[0]+v[1].upper() for k, v in MAPS.items()}
MAPS.update(maps1)
MAPS.update(maps2)
MAPS.update(maps3)

# Cần chỉ định là dùng unicode đối với python2
re.UNICODE

# Chỉ thay khi các vần trên không có q đứng trước và nó cũng là phần kết thúc của từ.
# Không thay nếu sau vần trên là ký tự tăng tốc [&_].
PAT_DAUKIEUMOI = re.compile(r'(?<!q)(%s)(?![a-zA-Z&_])' % '|'.join(MAPS.keys()), re.I)

def sub_kieucu(match):
    s = match.group(1)
    return MAPS[s]

def daukieucu(input_str):
    return PAT_DAUKIEUMOI.sub(sub_kieucu, input_str)

if __name__ == '__main__':
    script, filename = argv
    fd = open(filename, 'r')
    for line in fd:
        # dùng dấu phẩy để không in thêm ký tự dòng mới
        print daukieucu(line),
    fd.close()

