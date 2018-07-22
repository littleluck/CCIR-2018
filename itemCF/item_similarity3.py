import pandas as pd
import numpy as np
import pickle


fsimilarity = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix.txt', 'rb')
similarity = pickle.load(fsimilarity)
fsimilarity.close()

# K=50比K=100要好
K = 100

import time

for answer, similar_answer in similarity.items():
    start = time.clock()
    similarity[answer] = dict(sorted(similarity[answer].items(), key=lambda x: x[1], reverse=True)[:K])
    print(time.clock() - start)

f = open('D:\\CCIR2018\\itemCF\\item_similarity_matrix2.txt', 'wb')
pickle.dump(similarity, f)
f.close()

print("相似矩阵已生成！！！")

