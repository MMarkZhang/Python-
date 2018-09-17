#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:35:57 2018

@author: Mark
"""
from math import sqrt 

critics = {'Lisa Rose' : {'Lady in the Water' : 2.5, \
'Snakes on a Plane' : 3.5, 'Just My Luck' :3.0, \
'Superman Returns' : 3.5, 'You, Me and Dupree' : 2.5, \
'The Night Listener' : 3.0}, \
'Gene Seymour': {'Lady in the Water' : 3.0, \
'Snakes on a Plane': 3.5, 'Just My Luck' : 1.5, \
'Superman Returns' : 5.0, 'The Night Listener': 3.0, \
'You, Me and Dupree' : 3.5}, \
'Michael Philips' : {'Lady in the Water' : 2.5, \
'Snakes on a Plane': 3.0, \
'Superman Returns' : 3.5, 'The Night Listener': 4.0}, \
'Claudia Puig' : {'Snakes on a Plane': 3.5, \
'Just My Luck' : 3.0, 'The Night Listener': 4.5, \
'Superman Returns' : 4.0, 'You, Me and Dupree' : 2.5},\
'Mick LaSalle' : {'Lady in the Water' : 3.0, \
'Snakes on a Plane': 4.0, 'Just My Luck' : 2.0, \
'Superman Returns' : 3.0, 'The Night Listener': 3.0, \
'You, Me and Dupree' : 2.0}, \
'Jack Matthews' : {'Lady in the Water' : 3.0, \
'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, \
'Superman Returns' : 5.0, 'You, Me and Dupree' : 3.5}, \
'Toby' : {'Snakes on a Plane':4.5, \
'You, Me and Dupree' : 1.0 , 'Superman Returns' : 4.0}
}

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    n = len(si)    
    if len(si)==0: return 0 
    #算出对于各部电影评分的总和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    #对于电影评分平方，然后求和
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
    #两人对于同一电影评分的乘积，然后求和
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    num = pSum - (sum1*sum2/n) 
    den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))
    if den == 0: return 0 
    
    r = num/den #计算correlation coefficient 
    return r 

def topMatches(prefs, person, n=5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other),other) \
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]
    
def getRecommendations(prefs, person, similarity=sim_pearson) :
    totals = {}
    simSums = {}
    for other in prefs: 
        #不和自己做对比
        if other == person : continue 
        sim = similarity(prefs, person, other) #调用similarity计算各个人
        #忽略评价为零或者小于零的情况
        if sim <= 0 : continue 
        # 对于每部自己还没看的电影的计算
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0 :
                #计算加权总值
                totals.setdefault(item,0)
                totals[item] += prefs[other][item] * sim
                #计算用到的人的sim总值
                simSums.setdefault(item,0)
                simSums[item] += sim 
    #返回整理后的列表 dic.items用于遍历字典里的所有元祖数组
    rankings = [(total/simSums[item], item) for item, total in totals.items()]
    
    rankings.sort(reverse = True)
    return rankings 
    
def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{}) #setdefault必不可少
            result[item][person] = prefs[person][item]
    return result 

def calculateSimilarItems(prefs, n=10):
    #建立字典，给出最为相近的物品
    result = {}
    #调用之前的函数，使得矩阵倒置，以物品为中心
    itemPrefs = transformPrefs(prefs)
    c = 0 
    for item in itemPrefs:
        c += 1 
        if c%100 == 0: print ("%d / %d" %(c,len(itemPrefs)))
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_pearson)
        result[item] = scores 
    return result 









    
    