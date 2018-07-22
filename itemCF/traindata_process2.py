#!/usr/bin/python
#-*- coding: utf-8 -*-
 
##############################################################
# Copyright (c) 2018 USTC, Inc. All Rights Reserved
##############################################################
# File:    dataProcess.py
# Author:  haihua
# Date:    2018/07/12 02:21:53
# Brief:
##############################################################

import pandas as pd
import numpy as np
import pickle

# 从D:\\CCIR2018\\itemCF\\training.txt中提取需要的四列

def similarityCompute(path):
    
    import time

    count = 0
    with open('D:\\CCIR2018\\itemCF\\training_1.txt','w', encoding='utf-8') as f1:
        with open(path,'r', encoding='utf-8') as f:
            start = time.clock()
            while True:
                line=f.readline()
                count += 1
                if count%100000 == 0:
                    print(time.clock() - start)
                    start = time.clock()
                if not line:
                    break
                list1 = line.strip().split('\t')
                f1.write(list1[0]+'\t'+list1[2]+'\t'+list1[-3]+'\t'+list1[-1]+'\n')
    

if __name__ =='__main__':
    similarityCompute('D:\\CCIR2018\\itemCF\\training.txt')


        

















# vim: set expandtab ts=4 sw=4 sts=4 tw=100
