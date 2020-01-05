# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2020-01-05 09:54
# * Author : zhangsf
# *===================================*
# 多文件夹批量修改文件名
# 用 OS 模块的 listdir 方法枚举目录下的文件名，用列表切片过滤后缀，再用 rename 方法重命名文件
import os

path = '/Users/zhangsf/Movies/红楼梦/红楼梦001-060集'
count = 0
files_list = os.listdir(path)
print(files_list)  # 返回一个文件名列表

for file_name in os.listdir(path):
    # 切片获取文件扩展名
    if file_name[-3::] == 'mp3':
        count += 1
        # 新文件名控制
        # new_name = str(count) + '.mp3'
        # 因为获取的文件的顺序的时候没有按照事先排序的顺序，就截取原来文件的前面的部分进行重命名
        new_name = file_name[0:3] + '.mp3'
        print("before---文件名", file_name)
        print(" after---文件名", new_name)
        print("************************")
        # os.rename 的参数要写全文件路径
        os.rename(path + '/' + file_name, path + '/' + new_name)
print("文件夹：{0} 一共修改文件的个数为 {1}".format(path, count))