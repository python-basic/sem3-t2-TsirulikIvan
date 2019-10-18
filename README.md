# sem3-t2
Самостоятельная работа по теме №2

## Инвариантная:
  ### 2.1 Разработать скрипт с функцией, которая строит таблицу истинности для логического выражения (по вариантам) для двух и трех аргументов (используются различные наборы значений аргументов).
  ```python
  
  ```
  
   ### 2.2. Разработать программу, которая выводит на экран с помощью ASCII-графики таблицу истинности на основе переданных ей на вход аргументов (логическое выражение, аргументы, результат вычисления выражения). Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 
  ```python
  import math
alphabet = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

def wrap_str(args, exp, res):
  inf = ''
  for i in args:
    inf += wrap_wall(i)
  inf += wrap_wall(res, len(exp))
  return inf

def info_str(args, exp):
  inf = ''
  for i in range(len(args)):
    inf += wrap_wall(alphabet[i])
  inf += wrap_wall(exp)
  return inf
  
def wrap_wall(text, exp_long = 1):
  if (exp_long % 2 == 0):
    delt = math.ceil(exp_long / 2)
    tmp = '|' + delt * ' ' + text + (delt + 1) * ' ' + '|'
  else:
    delt = math.ceil(exp_long / 2)
    tmp = '|' + delt * ' ' + text + delt * ' ' + '|'
  return tmp

def tablet_form(expression, res, args):
  table_long = len(args) * 5 + len(expression) + 4
  print(table_long * '-')
  print(info_str(args, expression))
  print(table_long * '-')
  print(wrap_str(args, expression, res))
  print(table_long * '-')



le = input('Enter logic expression:\n')
result = input('Enter result of expression\n')
args = input('Enter arguments of expression (use space to divion args)\n')
args = tuple(args.split(' '))
print(le)
print(result)

tablet_form(le, result, args)
  ```
  
   ### 2.3. Разработать скрипт с функцией, которая для ряда Фибоначчи, где количество элементов, n = 22, возвращает подмножество значений или единственное значение (по вариантам). Для нахождения элемента требуется использовать слайсы. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 
  ```python
  
  ```
  
   ### 2.4. Напишите программу с функцией, в которой будет реализовано решение физической задачи (по вариантам). Например: ящик, имеющий форму куба с ребром a см без одной грани, нужно покрасить со всех сторон снаружи. Найдите площадь поверхности, которую необходимо покрасить. Ответ дайте в квадратных сантиметрах. Решение задачи оформите в виде функции square(a), которая возвращает значение s. Например, при значении a = 30, square(30) вернет s = 4500. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
  ```python
  
  ```
  
  
