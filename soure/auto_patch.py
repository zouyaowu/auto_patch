# -*- coding:utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        自动整理补丁
# Purpose:     支持 2007及以后的 xecel 版本
#
# Author:      zou.yw
#
# Created:     25/10/2017
# Modifiy:     14/11/2017
# Copyright:   (c) zou.yw 2017
# Licence:     GPL
#-------------------------------------------------------------------------------


from openpyxl import Workbook, load_workbook
import os
import re


def read_excel(data=None, read_type='row'):
    """
    参数：data=excel文件路径，read_type=row/column按行读还是按列读
    遍历excel文件，返回数据列表（默认按行）
    返回：包含元组的字典
    """

    try:
        # 打开文件
        workbook = load_workbook(data)
        # 获取所有sheet，返回列表，格式：[u'sheet1', u'sheet2']
        workbook_sheets_list = workbook.get_sheet_names()
        wb_sheets = {}
        for sheet_name in workbook_sheets_list:
            sheet = workbook.get_sheet_by_name(sheet_name)
            # 统计空行的数量，如果连续空一定数量行，则认为表格后面都是空的，跳过
            # 避免有些单元格设置了格式，但是没有实际数据时，会一直在遍历这些单元格
            null_cnt = 0
            sheet_all_rows = []
            if read_type =='row':
                sheet_item = sheet.rows
            else:
                sheet_item = sheet.columns
            # 遍历工作簿所有单元格
            for colu_row in sheet_item:
                # 遍历每行或列
                tmp = []
                # 遍历每个单元格
                for cel_index in range(len(colu_row)):
                    if colu_row[cel_index].value:
                        null_cnt = 0
                        tmp.append(colu_row[cel_index].value)
                        # print(sheet_all_rows)
                        # for cell in colu_row:
                    null_cnt +=1
                sheet_all_rows.append(tmp)

                # 连续10行空
                if null_cnt > 10:
                    break
            wb_sheets[sheet.title] = sheet_all_rows
    except Exception as err:
        print(err)
        return None
    return wb_sheets


def write_excel(data=None, file_name='./new_excel.xlsx'):
    """
    功能：把数据写入 excel
    入参：data=要写入的数据（支持 列表、元组、字符串）; file_name=要写入的文件
    返回值：写入成功 Ture; 写入失败 False
    """

    if not isinstance(data,list):
        # return "The data to write , not a list"
        return None
    # 新建一个工作簿（内存中），用来存放输出结果
    wb_new = Workbook()
    # 新建一张表
    ws_new = wb_new.active
    try:
        ws_new.append(data)
    except  Exception as bug:
        ws_new.append(['we have a problme. i have a bug'])
        ws_new.append([bug])
    finally:
        try:
            wb_new.save(file_name)
        except  Exception as err:
            print('无法保存文件，或许在编辑中')
    return


def data_format(data):
    """
    功能：对数据做格式化处理
    """
    try:
        if isinstance(data, list):
            for i in range(len(data)):
                tmp_data = str(tmp_data)
                tmp_data = data[i].lower()
                tmp_data = tmp_data.replace("\\\\","/")
                tmp_data = tmp_data.strip()
                data[i] = tmp_data
        else:
            tmp_data = str(tmp_data)
            tmp_data = tmp_data.lower()
            tmp_data = tmp_data.replace("\\\\","/")
            tmp_data = tmp_data.strip()
            data = tmp_data
        return data
    except Exception as err:
        print(err)
        return None

def get_file_list_patch(file_path=None):
    pass
    if not file_path:
        return None
    # 閬嶅巻鐩�綍
    file_set = set()
    for fpathe, dirs, fs in os.walk(file_path):
        file_set = file_set | set(fs)

    return (file_set)


def check_patch(file_path=None):
    file_list = get_file_list_patch(file_path)
    file_index = file_list.find('寰呴獙璇佽ˉ涓佹枃妗�xlsx')
    excel_data = read_excel(file_path + '/' + file_list[file_index])
    for key in excel_data:
        for cell in range(len(excel_data[key])):
            str_tmp = excel_data[cell]
            str_tmp = data_format(str_tmp)

    # 浠巈xcel鏁版嵁涓�彁鍙栧嚭绋嬪簭銆佽剼鏈�枃浠跺悕
    for i in excel_data:
        pass
    dll_trait = '瀵瑰簲DLL鏂囦欢'
    sql_trait = 'SQL鑴氭湰/鎶ヨ〃/鍏跺畠閰嶇疆鏂囦欢(鍚�矾寰�'
    dll_index = 0
    sql_index = 3


    # 鏁寸悊绋嬪簭銆佽剼鏈�泦
    sql_name_set = set()
    dll_name_set = set()
    for t in dll_set:
        if not t:
            continue
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        str_tmp = str_tmp.strip()
        if str_tmp[-4:-3] != '.':
            str_tmp += '.dll'
        dll_name_set.add(str_tmp.split('/')[-1])
    for t in sql_set:
        if not t:
            continue
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        str_tmp = str_tmp.strip()
        if str_tmp[-4:-3] != '.' and str_tmp[-4:] not in ('.sql', '.rps', '.xml'):
            str_tmp += '.sql'
        sql_name_set.add(str_tmp.split('/')[-1])

    # 鎶婃枃妗ｅ悕绉拌浆鎴愬垪琛�紝鏂逛究缁熻�鎵句笉鍒扮殑鏁版嵁
    dll_list = list(dll_name_set)
    sql_list = list(sql_name_set)

    # 閬嶅巻鐗堟湰鐩�綍
    file_list = set()
    for fpathe, dirs, fs in os.walk(file_path):
        file_list = file_list | set(fs)

    for i in file_list:
        file_name = i.lower()
        if file_name[-4:] != '.dll' and file_name[-4:] != '.sql':
            continue

        # 璇诲彇鍒扮殑鏂囦欢涓庢枃妗ｄ腑鐨勬枃浠跺仛閬嶅巻姣斿�
        for dll_tmp in dll_name_set:
            if file_name.lower() == dll_tmp.lower():
                dll_list.pop(dll_list.index(dll_tmp.lower()))
            else:
                pass
        for sql_tmp in sql_name_set:
            if file_name.lower() == sql_tmp.lower():
                sql_list.pop(sql_list.index(sql_tmp.lower()))
            else:
                pass
    if dll_list:
        print('dll miss ---> %s', dll_list)
    if sql_list:
        print('sql miss ===> %s', sql_list)

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
    for t in dll_set:
        if not t:
            continue
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        str_tmp = str_tmp.strip()
        if str_tmp[-4:-3] != '.':
            str_tmp += '.dll'
        dll_name_set.add(str_tmp.split('/')[-1])
    for t in sql_set:
        if not t:
            continue
        str_tmp = str(t).replace("\\\\","/")
        str_tmp = str_tmp.replace('\\','/')
        str_tmp = str_tmp.strip()
        if str_tmp[-4:-3] != '.' and str_tmp[-4:] not in ('.sql', '.rps', '.xml'):
            str_tmp += '.sql'
        sql_name_set.add(str_tmp.split('/')[-1])

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

        # 读取到的文件与文档中的文件做遍历比对
        for dll_tmp in dll_name_set:
            if file_name.lower() == dll_tmp.lower():
                dll_list.pop(dll_list.index(dll_tmp.lower()))
            else:
                pass
        for sql_tmp in sql_name_set:
            if file_name.lower() == sql_tmp.lower():
                sql_list.pop(sql_list.index(sql_tmp.lower()))
            else:
                pass
    if dll_list:
        print('dll miss ---> %s', dll_list)
    if sql_list:
        print('sql miss ===> %s', sql_list)

def read_excel_for_patch(excel_file=None, output='new.xlsx'):
    # 新建一个文件，用来存放输出结果
    wb_new = Workbook()
    # 新建一张表
    ws_new = wb_new.active
    # 新增一行表头
    ws_new.append(['版本新功能列表'])
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
                        bug_id = ''
                        demand_id = ''
                        bug_or_demand = str(j[bugid_index].value)
                        bug_or_demand = bug_or_demand.strip()
                        if bug_or_demand != 'None':
                            if str(bug_or_demand)[0:1].isalpha() and str(bug_or_demand)[0:3].lower() != 'bug':
                                demand_id = bug_or_demand
                            else:
                                bug_id = bug_or_demand
                        ws_new.append(['',bug_id,sheet.title,demand_id,'','',j[modification_index].value,'',''])
                row_flag +=1
    except  Exception as bug:
        ws_new.append(['we have a problme. i have a bug'])
        print(bug)
        print(j[bugid_index].value)
    finally:
        try:
            wb_new.save(output)
        except  Exception as err:
            print('无法保存文件，文件可能正在被编辑')
    return

if __name__ == '__main__':
    excel_file = r'\\Hk-office-fs01\品质管制部_内部文件$\客户升级版本\V1.27版本\补丁\服装版本\V1.27.15.001(2017-11-15)/V1.27.15.001(2017-11-15)补丁说明文档.xlsx'
    read_excel_for_patch(excel_file, 'V1.27.15.001产品新功能列表说明.xlsx')
    # excel_data = read_excel(excel_file)
    # print(excel_data['杩涢攢瀛�][0].index('淇�敼鏃ユ湡'))
    # file = r'D:\jobs\澶栧彂鐗堟湰\閫氱敤\V1.25\V1.25.18.001(2017-6-14)\V1.25.18.001(2017-6-14)琛ヤ竵璇存槑鏂囨。.xlsx'
    # check_path = r'\\Hk-office-fs01\鍝佽川绠″埗閮╛鍐呴儴鏂囦欢$\瀹㈡埛鍗囩骇鐗堟湰\V1.28鐗堟湰\琛ヤ竵\鏈嶈�鐗堟湰\寰呴獙璇佽ˉ涓�
    # file = check_path + '\V1.28鏈嶈�寰呴獙璇佽ˉ涓佹枃妗�xlsx'
    # check_dll_sql(file,check_path)
