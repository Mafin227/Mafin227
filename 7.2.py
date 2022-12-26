import os, datetime
date= datetime.datetime.now()
with open('about.txt', 'w') as file:
  file.write('My name is Anna.\n I`m 12 years old and I live and study in Ternopil.\n I study in School 5 in class 7B.\n ')
with open('about.txt', 'a') as file:
  file.write(f'\ndate - {date}')
with open('about.txt', 'r') as file:
  print(file.read())