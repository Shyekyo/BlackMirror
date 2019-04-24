#-*-coding:utf8-*-
"""
author:xiaofan
date:2019
"""
from __future__ import division
from recommenderSys.CF import reader
import math
import operator


def base_contribute_score():
    return 1
def update_one_contribute_score(user_total_click):
    return 1/math.log10(1+user_total_click)
def update_two_contribute_score(click_time_one,click_time_two):
    delata_time = abs(click_time_one-click_time_two)
    return 1/(1+delata_time)


def cal_item_sim(user_click,user_click_time,flag=0):
    """
    :param user_click: key user_id value [itemid1,itemid2]
    :return: dict key itemid i, value dict value_key itemid j,value_value simscore
    """
    co_appear = {}
    item_user_click_time ={}
    for user,itemlist in user_click.items():
        for index_i in  range(0,len(itemlist)):
            itemid_i = itemlist[index_i]
            item_user_click_time.setdefault(itemid_i,0)
            item_user_click_time[itemid_i] += 1
            for index_j in range(index_i+1,len(itemlist)):
                itemid_j = itemlist[index_j]
                if user+"_"+itemid_i not in user_click_time:
                    click_time_one = 0
                else:
                    click_time_one = user_click_time[user+"_"+itemid_i]
                if user+"_"+itemid_j not in user_click_time:
                    click_time_two = 0
                else:
                    click_time_two = user_click_time[user+"_"+itemid_j]
                co_appear.setdefault(itemid_i,{})
                co_appear[itemid_i].setdefault(itemid_j,0)
                if(flag==0):
                    co_appear[itemid_i][itemid_j] += base_contribute_score()
                elif(flag==1):
                    co_appear[itemid_i][itemid_j] += update_one_contribute_score(len(itemlist))
                else:
                    co_appear[itemid_i][itemid_j] += update_two_contribute_score(click_time_one,click_time_two)
                co_appear.setdefault(itemid_j,{})
                co_appear[itemid_j].setdefault(itemid_i,0)
                if(flag==0):
                    co_appear[itemid_i][itemid_j] += base_contribute_score()
                elif(flag==1):
                    co_appear[itemid_i][itemid_j] += update_one_contribute_score(len(itemlist))
                else:
                    co_appear[itemid_i][itemid_j] += update_two_contribute_score(click_time_one,click_time_two)

    item_sim_score = {}
    item_sim_score_sorted = {}
    for itemid_i,relate_item in co_appear.items():
        for itemid_j,co_time in relate_item.items():
            sim_score = co_time/math.sqrt(item_user_click_time[itemid_i]*item_user_click_time[itemid_j])
            item_sim_score.setdefault(itemid_i,{})
            item_sim_score[itemid_i].setdefault(itemid_j,0)
            item_sim_score[itemid_i][itemid_j] = sim_score
    for itemid in item_sim_score:
        item_sim_score_sorted[itemid] = sorted(item_sim_score[itemid].items(),\
                                               key=operator.itemgetter(1),reverse=True)

    return item_sim_score_sorted

def cal_recom_result(sim_info,user_click):
    """
    :param sim_info: item sim dict
    :param user_click: user click dict
    :return: dict key:userid value dict, value_key itemid,value_value recom_score
    """
    recent_click_num = 3
    topk = 5
    recom_info = {}
    for user in user_click:
        click_list = user_click[user]
        recom_info.setdefault(user,{})
        for itemid in click_list[:recent_click_num]:
            if itemid not in sim_info:
                continue
            for itemidsimzuhe in sim_info[itemid][:topk]:
                itemsimid = itemidsimzuhe[0]
                itemsiscore = itemidsimzuhe[1]
                recom_info[user][itemsimid] = itemsiscore
    return recom_info

def debug_itemsim(item_info,sim_info):
    """
    :param item_info: dict key itemid value[item,genres]
    :param sim_info: dict key itemid value dict key [(itemid1,score)]
    :return:
    """
    fixed_itemid = "1"
    [title_fix,genres_fix] =  item_info[fixed_itemid][:5]
    for zuhe in sim_info[fixed_itemid]:
        itemid_sim = zuhe[0]
        sim_score = zuhe[1]
        if itemid_sim not in item_info:
            continue
        [title,genres] = item_info[itemid_sim]
        print(title_fix + "\t" +genres_fix + "\t sim:" + title+"\t"+genres+ "\t"+str(sim_score))

def debug_recomresult(recom_result,item_info):
    """
    :param recom_result: key userid,value dict value_key item value value = score
    :param item_info: dict key itemid value[item,genres]
    """
    user_id="1"
    if user_id not in recom_result:
        return
    for zuhe in sorted(recom_result[user_id].items(),key=operator.itemgetter(1),reverse=True):
        itemid,score = zuhe
        if itemid not in item_info:
            continue
        print(",".join(item_info[itemid]) + "\t" + str(score))
def main_flow():
    user_click,user_click_time = reader.get_user_click("../../data/ml-100k/u1.base")
    item_info = reader.get_item_info("../../data/ml-100k/u.item")
    sim_info = cal_item_sim(user_click,user_click_time,2)
    debug_itemsim(item_info,sim_info)
    recom_result = cal_recom_result(sim_info,user_click)
    debug_recomresult(recom_result,item_info)
    print(recom_result["2"])
    print(recom_result["5"])

if __name__ =="__main__":
    main_flow()