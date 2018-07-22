import pandas as pd
import numpy as np
import pickle


fanswer = open('D:\\CCIR2018\\itemCF\\test_answers.txt', 'rb')
test_answers = pickle.load(fanswer)
ftrain = open('D:\\CCIR2018\\itemCF\\user_answer_test.txt', 'rb')
user_answer_test = pickle.load(ftrain)

fanswer.close()
ftrain.close()

import time
print(len(test_answers.keys()))
answer_user_test = {}
for answer in test_answers.keys():
    start = time.clock()
    for test_user in user_answer_test.keys():
        temp_dic = user_answer_test[test_user]
        if answer in temp_dic.keys():
            answer_user_test.setdefault(answer, []).append(test_user)
    print(time.clock() - start)

f = open('D:\\CCIR2018\\itemCF\\answer_user_test.txt', 'wb')
pickle.dump(answer_user_test, f)
f.close()

print(len(answer_user_test))
print("answer_user_test.txt字典已生成！！！")

