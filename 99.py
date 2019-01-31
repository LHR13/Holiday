import string #读取英文原著alice
path = 'E:/Python/data/NLP/alice.txt' with open(path,'r',encoding= 'utf-8') as text: #将所有的英文字母转换成小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()] #转换成集合形式
    words_index = set(words) #使用字典统计词频
    counts_dict = {index:words.count(index) for index in words_index} #按照词频从高到低排序
    for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
        if counts_dict[word] > 10:
            print('{} -- {} times'.format(word,counts_dict[word])) 
