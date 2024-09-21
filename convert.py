from opencc import OpenCC

# 创建转换器实例
cc = OpenCC('t2s')  # 从繁体转换为简体

# 读取繁体文档
with open('D:\\Text Mining Zhufanzhi\\Zhufanzhi_part 2_before.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 转换文本
converted = cc.convert(text)

# 将转换后的文本保存到新文件
with open('converted_part 2_after.txt', 'w', encoding='utf-8') as file:
    file.write(converted)

print("开始读取文件...")
with open('D:\\Text Mining Zhufanzhi\\Zhufanzhi_part 2_before.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print("文件读取完成。")
