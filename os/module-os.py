# coding:utf-8

"""
    @version:  
    @date:     2017/8/7 下午11:06
    @file:     module-os.py
    @software: PyCharm
    @auther:   aesthetic92
"""
import os

# 显示当前使用的平台
print os.name

# 显示当前python脚本工作路径
print os.getcwd()

# 返回指定目录下的所有文件和目录名
print os.listdir('./data')

# 删除一个文件
# os.remove('filename')

# 创建单个目录
# os.mkdir('test')

# 可生成多层递规目录
# os.makedirs('dirname/dirname')

# 删除单级目录
# os.rmdir('dirname')

# 重命名文件
# os.rename("oldname", "newname")

# 显示当前绝对路径
print os.path.abspath('./data')

# 返回该路径的父目录
print os.path.dirname('./data')

# 如果path是一个文件，则返回True
print os.path.isfile('./data')

# 如果path是一个目录，则返回True
print os.path.isdir('./data')

# 获取文件或者目录信息
print os.stat('./data')

# 将path分割成路径名和文件名。
# (事实上，如果你完全使用目录，
# 它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
# os.path.split('./data/test')     # ('/data', 'test')

# 连接目录与文件名或目录 结果为path/name
print os.path.join('data', 'test')

# 函数用来检验给出的路径是否真地存在
print os.path.exists('./data/test')