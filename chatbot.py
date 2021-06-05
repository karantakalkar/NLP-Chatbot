#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:20:58 2021

@author: karan takalkar
"""

import numpy as np
import tensorflow as tf
import re # used for text simplification
import time

### Data Pre Processing ###

# importing datasets
lines = open('movie_lines.txt', encoding = 'utf-8', errors='ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors='ignore').read().split('\n')

# dictionary that maps each line with it's id
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

# create a list of all conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
    conversations_ids.append(_conversation.split(','))
    
# Getting separately the questions and the answers
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        