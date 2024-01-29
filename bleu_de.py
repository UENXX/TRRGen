from nmt_bleu import compute_bleu

# 读入测试集的review
data_test = open('./data/rrgen_test_data.txt', 'r', encoding='UTF-8')
reviews = []
for item in data_test:
  try:
    temp = item.split('***')
    review = temp[5]
    reviews.append([review.strip().split()])
  except:
    continue

"""读入本模型输出数据"""
predicted_path = './result/noappname.txt'
reader = open(predicted_path, 'r')
result_list = reader.read().split('***')
result_list.pop()
prediction = []
for item in result_list:
  prediction.append(item.split())

"""读入RRGen数据"""
"""
predicted_path = './result/1111.txt'
reader = open(predicted_path, 'r')
prediction = []
for item in reader:
  try:
    temp = item.split('**')
    result = temp[1]
    prediction.append(result.split())
  except:
    continue
"""


print('Calculating...')
score, pls, _, _, _, _ = compute_bleu(reviews, prediction)
print('bleu-4 score: %f' % score)
print('pls: ', pls)
print(len(reviews), '  ', len(prediction))