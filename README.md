Python3批量修改文件名小工具

# Python3批量修改文件名小工具
## 初衷：
在下载文件夹中的文件名后缀命名太长，看着不舒服想着修改命名，可是文件太多，一个一个修改又太麻烦

## 修改的部分：
 1. **path为需要修改文件夹的目录比如** /Users/zhangsf/Movies/红楼梦/红楼梦001-060集
 2. **需要修改的文件的后缀，切片获取文件扩展名**比如 .mp3
 3. **新文件名控制，自己视情况设置**
## 注意事项：
1.**因为获取的文件的顺序的时候没有按照事先排序的顺序，就截取原来文件的前面的部分进行重命名**
2.**os.rename 的参数要写全文件路径**
## 具体思路
1.**单个文件夹  参考rename.py**
用OS模块的 listdir 方法枚举目录下的文件名，用列表切片过滤后缀，再用 rename方法重命名文件。
2.**多个文件夹嵌套 参考 rename2.py**
用OS模块的 listdir 方法枚举目录下的文件名，根据具体的文件层数来嵌套
## 效果图
CSDN链接: [link](https://zhangvalue.blog.csdn.net/article/details/103840520).
修改之前的文件名
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200105101957152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly96aGFuZ3ZhbHVlLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)
单个文件夹的情况 rename.py
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200105102322493.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly96aGFuZ3ZhbHVlLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)
多个文件夹嵌套循环进入  rename2.py
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200105112404918.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly96aGFuZ3ZhbHVlLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)
修改完成之后的效果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200105102347107.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly96aGFuZ3ZhbHVlLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)
## Github地址链接
[Github地址链接](https://github.com/zhangvalue/RenameFiles)


