import pandas as pd
import numpy as np
import pickle


ftrain = open('D:\\CCIR2018\\itemCF\\answer_user_train.txt', 'rb')
answer_user_train = pickle.load(ftrain)
ftrain.close()


# import time
top100_answers = {}
for answer in answer_user_train:
    top100_answers.setdefault(answer, 0)
    top100_answers[answer] = len(answer_user_train[answer])

temp_top100 = {}
for answer in top100_answers:
    key = str(answer)[0:4]+str(answer)[-4:]
    temp_top100.setdefault(key, 0)
    temp_top100[key] = top100_answers[answer]

temp_top100 = dict(sorted(temp_top100.items(), key=lambda x: x[1], reverse=True)[0:100])

f = open('D:\\CCIR2018\\itemCF\\top100_answers.txt', 'wb')
pickle.dump(temp_top100, f)
f.close()


print("top100_answers.txt字典已生成！！！")

