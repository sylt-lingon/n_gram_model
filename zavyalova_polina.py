import string
from numpy import random
from collections import defaultdict

NEW_TEXT_SIZE = 20

def clean_text(line):
    line = line.strip()
    res_line = ''
    for word in line:
        table = str.maketrans('', '', string.punctuation)
        word = word.translate(table)
        word = word.lower()
        res_line += word
    return res_line    

def get_words(line, words):
    s = line.split()
    for w in s:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

words = dict()
text = ''
#with open('romeo_and_juliet.txt') as f:
with open('alice_in_wonderland.txt') as f:
    for line in f:
        line = clean_text(line)
        text += line + ' '
        get_words(line, words)

# print(text)
print(words)

words_count = 0
for w in words:
    words_count += words[w]
print(words_count)

words_prob = dict()
for w in words:
    words_prob[w] = words[w] / words_count
print(words_prob)

words_pair = defaultdict(list)
text_list = text.split()
for i in range(len(text_list) - 1):
    w1 = text_list[i]
    w2 = text_list[i + 1]
    flag = False
    for k in range(len(words_pair[w1])):
        if words_pair[w1][k][0] == w2:
            words_pair[w1][k][1] += 1
            flag = True
            break
    if not flag:
        words_pair[w1].append([w2, 1])
print(words_pair)

word0 = random.choice(list(words.keys()), 1)[0]
new_text = word0
for i in range(1, NEW_TEXT_SIZE):
    p0 = random.randint(words[word0])
    p = 0
    for k in range(len(words_pair[word0])):
        p += words_pair[word0][k][1]
        if p > p0:
            break
    word0 = words_pair[word0][k][0]
    new_text += ' ' + word0

print(new_text)
        
    
