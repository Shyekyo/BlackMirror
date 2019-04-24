#-*-coding:utf8-*-
"""
author:xiaofan
"""
import threading
from time import sleep
from recommenderSys.CLMcode import readcsv
import jieba


lock = 0

def read():
    print("1   reading")
    while True:
        global lock
        if lock == 0:
            readcsv.readcsv("../data/departuredelays.csv")[0:10]
            print("succeed")
            lock =1
        else :
            print("read falied")
            sleep(5)

def write():
    print("1  writing")
    global lock
    while True:
        if lock==1:
            print("write ..")
            lock = 0
        else :
            print("read falied")
            sleep(5)


threads = []
t1 = threading.Thread(target=read,args=())
threads.append(t1)
t2 = threading.Thread(target=write,args=())
threads.append(t2)

#for t in threads:
    #t.setDaemon(True)
    #t.start()

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
sen="以前一直以为conda和pip的作用完全一样，甚至conda可以代替pip，但是最近安装jieba时发现，使用conda怎么都安装不了，会出现以下报错"
seg_list = jieba.cut(sen)
print(" ".join(seg_list))
