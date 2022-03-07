#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Bot2.py
#  
#  Copyright 2022 g <g@g-desktop>
#  
# BOT_CONFIG = {
#     "intents": { # Намерения пользователя
#         "hello": { # Поздороваться
#             "examples": ["Привет", "Добрый день", "Шалом", "Здрасте", "Здравствуйте", "Доброе время суток"],
#             "responses": ["Привет, человек", "И вам здрасте", "Йоу"],
#         },
#         "bye": {
#             "examples": ["Пока", "До свидания", "Досвидос", "Прощай"],
#             "responses": ["Счастливо", "До свидания", "Если что - возвращайтесь"]
#         },
#         "how_are_you": {
#             "examples": ["Как дела", "Что делаешь", "Какие делища", "Как поживаешь", "Чо как"],
#             "responses": ["Маюсь фигней", "Учу Python", "Смотрю вебинары Скиллбокс"],      
#         },
#     },
#     "failure_phrases": ["Йа ничо ни понил", "Что-то непонятно", "Я всего лишь бот, сформулируйте попроще"]
# }
import json # Импорт библиотеки JSON
config_file = open("config.json", "r") # Открытие файла
BOT_CONFIG = json.load(config_file) # Преобразование из JSON в структуру данных
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import re
import nltk
import random

def normalize(text): # Создаем функцию, которая выкинет знаки препинания и приведет текст к нижнему регистру
  text = text.lower() # "ПРиВЕт" => "привет"
  # Удалять из текста знаки препинания с помощью "Regular Expressions"
  punctuation = r"[^\w\s]" # выражение позволяет удалить все знаки препинания
  # ^ - "все кроме"
  # \w - "буквы"
  # \s - "пробелы"

  # Старое выражение = \W = "все кроме букв"
  return re.sub(punctuation, "", text) # Заменяем все что попадает под шаблон punctuation на пустую строку "" в тексте text

def isMatching(text1, text2): # Создаем функцию, которая посчитает похожи ли два текста
  text1 = normalize(text1)
  text2 = normalize(text2)
  distance = nltk.edit_distance(text1, text2) # Посчитаем расстояние между текстами (насколько они отличается)
  average_length = (len(text1) + len(text2)) / 2 # Посчитаем среднюю длину текстов
  return distance / average_length < 0.4

def getIntent(text): # Понимать намерение по тексту
  all_intents = BOT_CONFIG["intents"]
  for name, data in all_intents.items(): # Пройти по всем намерениям и положить название в name, и остальное в переменную data
    for example in data["examples"]: # Пройти по всем примерам этого интента, и положить текст в переменную example
      if isMatching(text, example): # Если текст совпадает с примером
        return name

def getAnswer(intent):
  responses = BOT_CONFIG["intents"][intent]["responses"]
  return random.choice(responses)

def bot(text): # Функция = Бот
  # Пытаемся опеределить намерение  
  intent = getIntent(text)

  if not intent: # Если намерение не найдено
     # ToDO: подключить модель машинного обучения (классификатор текстов)
     test = vectorizer.transform([text])
     intent = model.predict(test)[0] # По Х предсказать у, т.е. классифицировать 

  print("Intent =", intent)

  if intent: # Если намерение найдено - выдать ответ
    return getAnswer(intent)

  # Заглушка
  failure_phrases = BOT_CONFIG['failure_phrases']
  return random.choice(failure_phrases)

# тексты
X = []
# классы
y = []
# Задача модели = это по "Х" научиться находить "у"
for name, data in BOT_CONFIG["intents"].items():
  for example in data['examples']:
    X.append(example) # Собираем тексты в Х
    y.append(name) # Собираем классы в у

model = LogisticRegression() # Настройки
# model.fit(X_vectorized, y) # Модель научиться по Х определять у
LogisticRegression()
# test = vectorizer.transform(["Как дела у людей в чате Скиллбокс"])
# model.predict(test) # По Х предсказать у, т.е. классифицировать
# array(['mood'], dtype='<U29')
# model.score(X_vectorized, y)
while 1:
	question = input('?') # Вопрос, который мы задаем боту
	if question=='q' or question=='стоп':
		break
	else:
		text=normalize(question)
		Answer=bot(text)
		print(Answer)

print('Пока пока')
