#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def filter(text): # Создаем функцию, которая выкинет знаки пре и приведет текст к нижнему регистру
  text = text.upper() #"Привет" => "ПРИВЕТ"
  punctuation = r"\W"
  #return text
  # Удалять из текста знаки препинания с помощью "Regular Expr"
  return re.sub(punctuation, "", text)# Заменяем все что попад
message=input('?=')
message=str(filter(message))
print(message)
output=''
value=0
for letter in message:
    if letter.isupper():
        value=ord(letter)-13
        letter=chr(value)
    if not letter.isupper():
        value=value+26
        letter=chr(value)
    output=output+letter
print(output)
file=open('password.txt', 'a')
file.write('\n'+output)
file.close()
input("End")
