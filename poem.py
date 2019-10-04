# coding: utf-8
import numpy as np
import matplotlib as plt
import pandas as pd
from numpy.random import randint
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
words
phrase = words.split('\n')
from numpy.random import choice
n = randint(3, 5)

for i in range(n):
    k = randint(3, 5)
    egg = choice(phrase, k)
    ham = ' '.join(egg)
    print(ham)
