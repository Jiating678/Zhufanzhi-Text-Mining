from jiayan import load_lm
from jiayan import CharHMMTokenizer
from jiayan import CRFPOSTagger
import pandas as pd
import xlwt

# 输入语料
with open('converted_zhufanzhi.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 利用kenlm模型分词
lm = load_lm('jiayan.klm')
tokenizer = CharHMMTokenizer(lm)
# print(list(tokenizer.tokenize(text)))

# 词性标注
words = list(tokenizer.tokenize(text))

postagger = CRFPOSTagger()
postagger.load('pos_model')
print(postagger.postag(words)) # list()

cut_postagger = zip(list(tokenizer.tokenize(text)),postagger.postag(words))
# print(list(cut_postagger))

# 词频统计
print(pd.Series(list(tokenizer.tokenize(text))).value_counts().head(1000))

#将分词、词性分析、词频统计结果保存到excel表格中
f = xlwt.Workbook('encoding = utf-8')  # 设置工作簿编码
sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet工作表
list1 = list(tokenizer.tokenize(text))  # list1为分词结果
list2 = postagger.postag(words)# list2为词性分析结果

for i in range(len(list1)):
    sheet1.write(i, 0, list1[i])  # 写入数据参数对应 行, 列, 值

for i in range(len(list2)):
    sheet1.write(i, 1, list2[i])
f.save('text.xls')  # 保存.xls到当前工作目录