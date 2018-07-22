import pandas as pd
import numpy as np
import pickle


answer_id = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\answer_id.dict', header=None)
answer_dict = {}
for row in range(0, answer_id.iloc[:, 0].size):
    answer_dict[str(answer_id.iloc[row, 0])] = answer_id.iloc[row, 1]

# print(answer_dict[list(answer_dict.keys())[0]])
# print(answer_dict[200774319])
# print(answer_dict.keys())

# question_id = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\question_id.dict')

candidate_df = pd.read_table('D:\\CCIR2018\\newdata\\competition.zip\\candidate.txt', header=None)
candidate = {}
for row in range(0, candidate_df.iloc[:, 0].size):
    candidate[candidate_df.iloc[row, 1]] = 1

dic = {}
test_answers = {}
test = pd.read_table('D:\\CCIR2018\\newdata\\updated_testing_set_135089.txt\\testing_set_135089.txt', header=None)
print(test.iloc[0, 0])
# import time
for row in range(0, test.iloc[:, 0].size):
    # start = time.clock()
    if '|' in str(test.iloc[row, 2]):
        # print(test.iloc[row, 0])
        reading_records = str(test.iloc[row, 2]).strip()
        # print(reading_records)
        userid = test.iloc[row, 0]
        records = reading_records.split(',')
        for record in records:
            docID = record.split('|')[0]
            reading_time = record.split('|')[2]
            if 'A' in docID:
                # print(docID)
                realID = answer_dict[docID[1:]]
                if realID in candidate.keys():
                    temp_dic = dic.get(userid, {})
                    temp_dic[realID] = reading_time
                    dic[userid] = temp_dic

                    test_answers[realID] = 1

    # print(time.clock() - start)


# 将每个用户看过的文章根据时间从大到小排序
for test_user in dic.keys():
    temp = dic[test_user]
    temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True)) # sorted之后变为列表
    dic[test_user] = temp


# f = open('D:\\CCIR2018\\user_answer_test.txt', 'wb')
f = open('D:\\CCIR2018\\itemCF\\user_answer_test.txt', 'wb')
pickle.dump(dic, f)
f.close()

f = open('D:\\CCIR2018\\itemCF\\test_answers.txt', 'wb')
pickle.dump(test_answers, f)
f.close()

print("user_answer_test.txt字典已生成！！！")

