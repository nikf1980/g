#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Bot.py
#  
#  Copyright 2022 g <g@g-desktop>
# 1. Искать "неточное" совпадение
import nltk
import re
import random
# Список вопросов и ответов
database=[
	{
      "question": "Как дела",
      "answer": ["Дела отлично", "Дела фиолетово", "Все шикарно", "Цветем и пахнем"],
	},
	{
      "question": "Как тебя зовут",
      "answer": ["Меня зовут Скиллбот", "Меня никак не зовут", "А ты сам сначала представься"],
	},
	{
      "question": "Какого цвета небо",
      "answer": ["Небо цвета голубого", "The sky is blue", "Не знаю"],
	},
	{
      "question": "ты кто",
      "answer": ["Бот", "Чат Бот", "А Вы кто?"],
	},
	{
      "question": "Как зовут",
      "answer": ["Меня зовут Скилл бот", "Я Бот на Питон", "А ты сам сначала представься, Кто?"],
	},
	{
      "question": "человек",
      "answer": ["а я Скилл бот", "как Вас зовут?", "А Ваше имя, Как?"],
	},
	{
      "question": "Николай",
      "answer": ["Приятно познакомиться", "Очень хорошо", "Красивое имя-:"],
	},
	{
      "question": "Что ты умеешь?",
      "answer": ["Разговаривать", "Поддержать беседу", "Чатиться в телеграмм"],
	},
	{
      "question": "Привет",
      "answer": ["Привет Привет", "Здравствуйте", "Что-то хотели?"],
	},
	{
      "question": "Программист",
      "answer": ["Это Вы меня написали?", "Очень хорошо", "Здорово, а я Бот"],
	}
]

def filter(text): # Создаем функцию, которая выкинет знаки препинания и приведет текст к нижнему регистру
  text = text.lower() # "ПРиВЕт" => "привет"
  # Удалять из текста знаки препинания с помощью "Regular Expressions"
  punctuation = r"\W" # выражение позволяет удалить все знаки препинания
  return re.sub(punctuation, "", text) # Заменяем все что попадает под шаблон punctuation на пустую строку "" в тексте text

def matchText(text1, text2): # Создаем функцию, которая посчитает похожи ли два текста
  text1 = filter(text1)
  text2 = filter(text2)
  distance = nltk.edit_distance(text1, text2) # Посчитаем расстояние между текстами (насколько они отличается)
  average_length = (len(text1) + len(text2)) / 2 # Посчитаем среднюю длину текстов
  return distance / average_length # Примерно насколько тексты отличаются в процентах 
def Fanswer():
	for pair in database:
		if matchText(question, pair["question"]) < 0.4:
			answer = random.choice(pair["answer"])
			print(answer)
   
while 1:
	question = input('?') # Вопрос, который мы задаем боту
	if question=='q' or question=='стоп':
		break
	else:
		Fanswer()

print('Пока пока')
