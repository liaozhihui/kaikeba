# 使用并查集，求句子相似度

# 并查集合并
def union(word1, word2):
    x = find(word1)
    y = find(word2)
    if x != y:
        map[x] = y

# 查找帮主
def find(word):
    while word in map and map[word] != word:
        # 向上找到父亲节点
        word = map[word]
    return word

# 判断两个单词是否相似
def is_similar(words1, words2, pairs):
    # 长度如果不相等
    if len(words1) != len(words2):
        return False
    # 插入到并查集
    for pair in pairs:
        union(pair[0], pair[1])
    # 判断word1, word2中每个单词的帮主是否一致（相同含义）
    for i in range(len(words1)):
        if find(words1[i]) != find(words2[i]):
            return False
    return True

# 记录每个节点的父亲节点
map = {}
words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
print(is_similar(words1, words2, pairs))

words1 = ["great"]
words2 = ["great"]
pairs = []
print(is_similar(words1, words2, pairs))
