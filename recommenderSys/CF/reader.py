#-*-coding:utf8-*-
"""
author:xiaofan
date:2019
"""
import os
def get_user_click(rating_file,flag=False):
    """
    :param rating_file: input file
    :return: dict key:userid,value[item1,item2...]
    """
    if not os.path.exists(rating_file):
        return {}
    user_click = {}
    user_click_time ={}
    fp = open(rating_file)
    for line in fp:
        item = line.strip().split("\t")
        if len(item)<4:
            continue
        [userid,itemid,rating,timestamp] = item
        if userid+"_"+itemid not in user_click_time:
            user_click_time[userid+"_"+itemid] = int(timestamp)
        if float(rating) < 3.0:
            continue
        if userid not in user_click:
            user_click[userid]=[]
        user_click[userid].append(itemid)
    fp.close()
    return user_click,user_click_time


def get_item_info(item_file):
    """
    :param item_file: input file
    :return: dict key itemid, value[title,genres]
    """
    mapping = ["unknown","Action","Adventure","Animation","Children's","Comedy",
               "Crime","Documentary","Drama","Fantasy","Film-Noir","Horror",
               "Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
    item_info ={}
    if not os.path.exists(item_file):
        print("there is no file")
        return {}
    fp = open(item_file,"r",encoding="utf8")
    for line in fp:
        item = line.strip().split("|")
        if len(item)<24:
            continue
        [itemid,item_title,release_date,video_release_date,IMDb_URL,
         unknown,Action,Adventure,Animation, Childrens,Comedy,Crime,Documentary,
         Drama,Fantasy,Film_Noir,Horror,Musical,Mystery,Romance,Sci_Fi,Thriller,
         War,Western] = item
        genres = ""
        mid_item = item[5:]
        index_count=0
        for i in mid_item:
            if i=="1":
                genres += mapping[index_count]+"|"
            index_count += 1
        genres=genres[0:-1]
        if itemid not in item_info:
            item_info[itemid]=[item_title,genres]
    fp.close()
    return item_info

if __name__ =="__main__":
    user_click = get_user_click("../../data/ml-100k/u1.base")
    print(len(user_click))
    print(len(user_click["1"]))
