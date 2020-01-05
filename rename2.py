# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2020-01-05 10:36
# * Author : zhangsf
# *===================================*
import os

path = '/Users/zhangsf/Movies/红楼梦/'
# 定义一个变量来控制文件的顺序
count = 0
files_list = os.listdir(path)
print(files_list)  # 返回一个文件名列表
for files in files_list:
    print(files)
    # 排除掉文件夹中自带的隐藏文件夹,.DS_Store目的在于存贮目录的自定义属性
    if files.__contains__(".DS_Store"):
        continue
    else:
        print("当前进入文件夹为", path + files)
        for file_name in os.listdir(path + files):
            # 切片获取文件扩展名,因为mp3的长度为3，如果是rmvb格式，那么长度就为4,以此类推
            if file_name[-3::] == 'mp3':
                count += 1
                # 新文件名控制
                # new_name = str(count) + '.mp3'
                # 因为获取的文件的顺序的时候没有按照事先排序的顺序，就截取原来文件的前面的部分进行重命名
                new_name = file_name[0:3] + '.mp3'
                # print("变量1", file_name, "变量2", new_name)
                # print("变量1：%s 变量2：%s" % (file_name, new_name))
                # print('变量1：{0}   变量2：{1}'.format(file_name, new_name))
                print('"before-文件名："{0}   "after-文件名："{1}'.format(file_name, new_name))
                # os.rename 的参数要写全文件路径
                os.rename(path + '/' + files + '/' + file_name, path + '/' + files + '/' + new_name)
        print("文件夹：{0} 一共修改文件的个数为 {1}".format(path + files, count))
        count = 0
