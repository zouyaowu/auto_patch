#-------------------------------------------------------------------------------
# Name:        自动整理补丁
# Purpose:
#
# Author:      zou.yw
#
# Created:     25/10/2017
# Copyright:   (c) zou.yw 2017
# Licence:     GPL
#-------------------------------------------------------------------------------

from openpyxl import Workbook, load_workbook
import os
import re

def check_dll_sql(excel_file, file_path):
    # 在文件中提取 dll、脚本名称，通过集合去重
    dll_set = set()
    sql_set = set()
    workbook = load_workbook(excel_file)
    workbook_sheets_list = workbook.get_sheet_names()
    dll_trait = '对应DLL文件'
    sql_trait = 'SQL脚本/报表/其它配置文件(含路径)'
    dll_index = 0
    sql_index = 3
    for i in workbook_sheets_list:
        sheet = workbook.get_sheet_by_name(i)
        # 遍历工作簿所有单元格
        row_flag = 1
        for j in sheet.rows:
            # 第一行是标题栏
            if row_flag == 1:
                for k in range(len(j)):
                    if j[k].value == dll_trait:
                        dll_index = k
                    elif j[k].value == sql_trait:
                        sql_index = k
            else:
                # 剔除空白行
                if j[dll_index].value:
                    dll_tmp = str(j[dll_index].value).lower()
                    dll_tmp = dll_tmp.split('\n')
                    dll_set |= set(dll_tmp)
                if j[sql_index].value:
                    sql_tmp = str(j[sql_index].value).lower()
                    sql_tmp = sql_tmp.split('\n')
                    sql_set |= set(sql_tmp)
            row_flag += 1

    # 整理程序、脚本集
    sql_name_set = set()
    dll_name_set = set()
    for t in sql_set:
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        if str_tmp[-4:] != '.sql':
            str_tmp += '.sql'
        sql_name_set.add(str_tmp.split('/')[-1])
    for t in dll_set:
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        if str_tmp[-4:] != '.dll':
            str_tmp += '.dll'
        dll_name_set.add(str_tmp.split('/')[-1])

    # 把文档名称转成列表，方便统计找不到的数据
    dll_list = list(dll_name_set)
    sql_list = list(sql_name_set)

    # 遍历版本目录
    file_list = set()
    for fpathe, dirs, fs in os.walk(file_path):
        file_list = file_list | set(fs)

    for i in file_list:
        file_name = i.lower()
        if file_name[-4:] != '.dll' and file_name[-4:] != '.sql':
            continue
        # file_name = i.replace('.dll','')
        # file_name = file_name.replace('.sql','')
        # 读取到的文件与文档中的文件做遍历比对
        for dll_tmp in dll_name_set:
            if file_name.lower() in dll_tmp.lower():
                # print("local_dll %s in dll_set" % file_name)
                dll_list.pop(dll_list.index(dll_tmp.lower()))
            else:
                # print("%s no in %s" % (file_name, dll_tmp))
                pass
        for sql_tmp in sql_name_set:
            if file_name.lower() in sql_tmp.lower():
                print("local_sql %s in sql_set" % file_name)
                print(sql_list)
                sql_list.pop(sql_list.index(sql_tmp.lower()))
            else:
                # print("%s no in %s" % (file_name, sql_tmp))
                pass
    if dll_list:
        print('can not find this %s', dll_list)
    if sql_list:
        print('can not find this %s', sql_list)
    # print(file_list)
    # print(dll_name_set)
    # print(sql_name_set)

def read_excel(excel_file):
    # 新建一个文件，用来存放输出结果
    wb_new = Workbook()
    # 新建一张表
    ws_new = wb_new.active
    # 新增一行表头
    ws_new.append(["序号","类型","系统模块","恒康需求编号","客户需求编号","涉及的客户","功能名称/修改说明","对现有业务的影响","备注"])

    try:
        # 打开文件
        workbook = load_workbook(excel_file)
        # 获取所有sheet，返回列表，格式：[u'sheet1', u'sheet2']
        workbook_sheets_list = workbook.get_sheet_names()
        # print(workbook_sheets_list)
        # 根据特定字段来查找需要的内容
        bugid_trait = '问题/需求编号'
        modification_trait = '功能/问题修改说明'
        bugid_index = 1
        modification_index = 2
        for i in workbook_sheets_list:
            sheet = workbook.get_sheet_by_name(i)
            # 遍历工作簿所有单元格
            row_flag = 1
            for j in sheet.rows:
                # 第一行是标题栏
                if row_flag == 1:
                    for k in range(len(j)):
                        if j[k].value == bugid_trait:
                            bugid_index = k
                        elif j[k].value == modification_trait:
                            modification_index = k
                else:
                    # 剔除空白行
                    if j[bugid_index].value or j[modification_index].value:
                        ws_new.append(['',j[bugid_index].value,sheet.title,'','',j[modification_index].value,'',''])
                row_flag +=1
    except bug:
        ws_new.append(['we have a problme. i have a bug'])
        ws_new.append([bug])
    finally:
        try:
            wb_new.save("new.xlsx")
        except err:
            print('无法保存文件，文件可能正在被编辑')

    return

if __name__ == '__main__':
    # excel_file = r'./V1.27.12.001(2017-10-25)补丁说明文档.xlsx'
    # read_excel(excel_file)
    file = r'D:\jobs\外发版本\通用\V1.25\V1.25.18.001(2017-6-14)\V1.25.18.001(2017-6-14)补丁说明文档.xlsx'
    path = r'D:\jobs\外发版本\通用\V1.25\V1.25.18.001(2017-6-14)'
    check_dll_sql(file,path)
