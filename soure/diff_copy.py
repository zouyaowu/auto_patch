# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        提取2个文件夹差异的内容，把差异（不一样、多出来的）的拷贝出来
#
# Author:      zou.yw
#
# Created:     05/01/2018
# Modifiy:     
# Copyright:   (c) zou.yw 2018
# Licence:     GPL
#-------------------------------------------------------------------------------


import os
from filecmp import  cmp


def diff(s_path, t_path):
    diff_file = set() 
    for fpath, dirs, fs in os.walk(t_path):
        for file in fs:
            taget_file = os.path.join(fpath, file)
            if s_path[-1] == '/' or s_path[-1] == '\\':
                s_path = s_path[0:-1]
            if t_path[-1] == '/' or t_path[-1] == '\\':
                t_path = t_path[0:-1]           
            
            # taget_file
            base_file = s_path + taget_file.replace(t_path, '')
            try:
                if not cmp(taget_file, base_file):
                    diff_file.add(taget_file)
            except:
                diff_file.add(taget_file)
    return diff_file


if __name__ == '__main__':
    path1 = r'D:\jobs\AutoTest\auto_patch\test_case\1'
    path2 = r'D:\jobs\AutoTest\auto_patch\test_case\2'
    path3 = r'D:\jobs\AutoTest\auto_patch\test_case\3\\'
    file = diff(path1, path2)
    for i in file:
        print(i)
        os.system("xcopy %s %s" % (i, path3))