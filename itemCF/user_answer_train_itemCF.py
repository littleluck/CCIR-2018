import pandas as pd
import numpy as np
import pickle


answer_id = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\answer_id.dict', header=None)
answer_dict = {}
for row in range(0, answer_id.iloc[:, 0].size):
    answer_dict[str(answer_id.iloc[row, 0])] = answer_id.iloc[row, 1]


candidate_df = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\candidate.txt', header=None)
candidate = set()
for row in range(0, candidate_df.iloc[:, 0].size):
    candidate.add(candidate_df.iloc[row, 1])

dic = {}
train_answers = set()
train = pd.read_table('D:\\CCIR2018\\itemCF\\training_1.txt', header=None)
# import time
for row in range(0, train.iloc[:, 0].size):
    # start = time.clock()
    userid = train.iloc[row, 0]
    if '|' in str(train.iloc[row, 1]):
        # print(test.iloc[row, 0])
        reading_records = str(train.iloc[row, 1]).strip()
        # print(reading_records)
        records = reading_records.split(',')
        for record in records:
            docID = record.split('|')[0]
            reading_time = record.split('|')[2]
            if 'A' in docID:
                # print(docID)
                realID = answer_dict[docID[1:]]
                if realID in candidate:
                    temp_dic = dic.get(userid, {})
                    temp_dic[realID] = reading_time
                    dic[userid] = temp_dic

                    train_answers.add(realID)
    if train.iloc[row, 3] in candidate:
        temp_dic = dic.get(userid, {})
        temp_dic[train.iloc[row, 3]] = str(train.iloc[row, 2])
        dic[userid] = temp_dic

        train_answers.add(train.iloc[row, 3])

    # print(time.clock() - start)

print('--------------------')

# 将每个用户看过的文章根据时间从大到小排序
for test_user in dic.keys():
    temp = dic[test_user]
    temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True)) # sorted之后变为列表
    dic[test_user] = temp


# f = open('D:\\CCIR2018\\user_answer_test.txt', 'wb')
f = open('D:\\CCIR2018\\itemCF\\user_answer_train.txt', 'wb')
pickle.dump(dic, f)
f.close()

# 此处train_answers是一个集合set
f = open('D:\\CCIR2018\\itemCF\\train_answers.txt', 'wb')
pickle.dump(train_answers, f)
f.close()

print(len(train_answers))
print("user_answer_train.txt字典已生成！！！")

