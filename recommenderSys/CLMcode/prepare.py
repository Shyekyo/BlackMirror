#--*--coding:utf8--*--
"""
author:xiaofan
"""

import jieba
import os

class Prefile:
    file_one_path = "../data/football.txt"
    file_one = open(file_one_path,"r",encoding="utf8")
    file_two_path = "../data/pig.txt"
    file_two = open(file_two_path,"r",encoding="utf8")
    file_three_path = "../data/Manchester.txt"
    file_three = open(file_three_path,"r",encoding="utf8")
    stop_word_path = "../data/stopword.txt"
    stop_word = open(stop_word_path,"r",encoding="utf8")
    stopword_list = []
    def __init__(self):
        print("obj is ready")
        self.del_cut_index()
        self.stop_word_list()
        rsu_one = self.tag(self.file_one,2)
        self.save(rsu_one,"football.txt")
        rsu_two = self.tag(self.file_two)
        self.save(rsu_two,"pig.txt")
        rsu_three = self.tag(self.file_three)
        self.save(rsu_three,"Manchester.txt")

    def stop_word_list(self,file=stop_word):
        for word in file.read():
            self.stopword_list.append(word)
    def tag(self,file,count=2):
        result = {}
        filter_result ={}
        for line in file.readlines():
            seg_list = jieba.cut(line)
            for seg in seg_list:
                if seg not in result.keys():
                    result[seg] = 0
                result[seg] += 1
        for k,v in result.items():
            if v > count and k not in self.stopword_list:
                filter_result[k]=v
        file.close()
        return filter_result
    def read(self):
        pass
    def build(self):
        pass
    def save(self,res,fn,path="../data/cut_index.txt"):
        with open(path,"a",encoding="utf8") as f:
            for k,v in res.items():
                line = "filename :"+fn+"\t"+k+"\t"+str(v)+"\r\n"
                f.write(line)
        f.close()
    def del_cut_index(self,path="../data/cut_index.txt"):
        if(os.path.exists(path)):
            os.remove(path)

if __name__ == "__main__":
    p = Prefile()