#импортируем нужные библиотеки
import string
from numpy import random
from collections import defaultdict

#задаем размер генерируемого текста
NEW_TEXT_SIZE = 20

#убираем из строки текста знаки препинания
def clean_text(line):
    line = line.strip()
    res_line = ''
    for word in line:
        table = str.maketrans('', '', string.punctuation)
        word = word.translate(table)
        word = word.lower()
        res_line += word
    return res_line    

#создаем словарь уникальных слов и считаем кол-во раз употребления каждого из слов
def get_words(line, words):
    s = line.split()
    for w in s:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

words = dict()
text = ''

#читаем файл, на основе которого будет генироваться текст, очищаем от знаков препинания и создаем словарь уникальных слов текста
with open('harry_potter_1.txt', encoding = 'Windows 1251') as f:
    for line in f:
        line = clean_text(line)
        text += line + ' '
        get_words(line, words)

#создаем словарь возможных пар слов и количество употребления каждой из пар
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

#выбираем первое слово и генерируем текст
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

#выводим сгенерированный текст
print(new_text)
        
    
