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

# 从原始训练集中提取出用户在测试集中的记录

def similarityCompute(path):
    test_users = set()
    test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
    # import time
    for row in range(0, test.iloc[:, 0].size):
        test_users.add(test.iloc[row, 0])
    
    import time

    count = 0
    with open('D:\\CCIR2018\\itemCF\\training.txt','w', encoding='utf-8') as f1:
        with open(path,'r', encoding='utf-8') as f:
            while True:
                start = time.clock()
                line=f.readline()
                count += 1
                if count%1000000 == 0:
                    print(time.clock() - start)
                if not line:
                    break
                if line.split('\t')[0] in test_users:
                    f1.write(line.strip()+'\n')
                    line=''
                    # line=line.strip().split('\t')
                    # # tmp=line[-1]
                    # tmpline+=line[0]+'\t'+line[2]+'\t'+line[-3]+'\t'+line[-1]+'\n'
    

if __name__ =='__main__':
    similarityCompute('D:\\CCIR2018\\newdata\\competition.zip\\training_set.txt')


        

















# vim: set expandtab ts=4 sw=4 sts=4 tw=100
