import pandas as pd
import numpy as np
import pickle


test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
print(test.iloc[0, 0])
# import time
users = set()
for row in range(0, test.iloc[:, 0].size):
    users.add(test.iloc[row, 0])

# 此处test_user.txt保存的是一个集合set
f = open('D:\\CCIR2018\\itemCF\\test_user.txt', 'wb')
pickle.dump(users, f)
f.close()
