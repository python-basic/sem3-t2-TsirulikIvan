# sem3-t2
Самостоятельная работа по теме №2

## Инвариантная:
  ### 2.1 Разработать скрипт с функцией, которая строит таблицу истинности для логического выражения (по вариантам) для двух и трех аргументов (используются различные наборы значений аргументов).
  ```python
A = False 
B = False 
C = False 
def log_func (x,y,z): 
    tmp1 = x or (y and z) 
    tmp2 = (x or y) and (x or z) 
    return str(int((not(tmp1)or tmp2)and(tmp1 or not(tmp2)))) 
def log_func2 (x,z): 
    tmp1 = not(x or not(z) and x) 
    tmp3 = not(x) and z 
    tmp2 = not(not(tmp3)or z) 
    return str(int((not (tmp1) or tmp2) and (tmp1 or not (tmp2)))) 
print(chr(172) + chr(741) + chr(745) + chr(866) + chr(709) + chr(708) + chr(8660)) 
print("-"*53) 
print("| A | B | C |" + " A"+chr(709)+"(B"+chr(708)+"C)" + 
chr(8660)+"(A"+chr(709)+"B)"+chr(708)+ "(A"+chr(709)+"C) |") 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
print("-"*53) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,(C)) + " "*12 + "|") 
print("-"*53) 
B = True 
C = False 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
B = True 
C = True 
print("-"*53)    
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
A = True 
B = False 
C = False 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
C = True 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
B = True 
C = False 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
C = True 
print("-"*53) 
print("| "+ str(int(A)) + " | " + str(int(B)) + " | " + str(int(C)) + " | " + log_func(A,B,C) + " "*12 + "|") 
print("-"*53) 
print(""*53) 
print(" "*53) 
print("-"*44) 
A = False 
C = False 
print("| A | C |" + " " + chr(172) +"(A" +chr(709)+chr(172)+"C"+chr(708)+ "A)" 
+ chr(8660)+ chr(172)+"("+chr(172)+ "A"+chr(708)+"C"+chr(8594)+"C ) |") 
print("-"*44)
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
A = True 
C = False 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44) 
C = True 
print("| "+ str(int(A)) + " | " + str(int(C)) + " | " + log_func2(A,C) + " |") 
print("-"*44)

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
def fibb(subset_st=0, subset_end=22):
    f_numbers = [0, 1]
    n = 22
    for i in range(2,n):
      f_numbers.append(f_numbers[i - 2] + f_numbers[i - 1])
    return f_numbers[subset_st:subset_end:]

start_p = int(input('Enter the first Number of subset\n'))
end_p = int(input('Enter the last Number of subset\n'))
print(fibb(start_p, end_p))
  ```
  
   ### 2.4. Напишите программу с функцией, в которой будет реализовано решение физической задачи (по вариантам). Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
   Постановка задачи: Определите начальную скорость бруска, если известно, что после того, как он проехал 0,5 м вниз по наклонной плоскости с углом наклона 30° к горизонту, его скорость стала равна 3 м/с. Трением пренебречь. Ответ приведите в м/с.
  ```python
  import math

def find_velocity(l=0.5, end_v=3, deg=30):
    h = l * math.sin(deg * math.pi / 180)
    print(l, h, end_v)
    return math.sqrt(end_v * end_v - 2 * 9.8 * h)

print(find_velocity())
  ```
  ## Вариативная:
  ### 2.1. Исследовать способы проверки программного кода Python на совместимость со стандартом PEP8. Составить сравнительную таблицу с анализом. Сформировать отчет, опубликовать отчет и таблицу в портфолио.
  
|    Способ проверки   |                                       +                                      |                                 -                                |
|:--------------------:|:----------------------------------------------------------------------------:|:----------------------------------------------------------------:|
|        Онлайн        | 1. Кроссплатформенность 2. Не требует доп установки 3. Прост в использовании |   1. Необходимость соединения с сетью 2. Требуется готовый код   |
| Плагин для редактора |          1.Подсветка во время кодинга 2.Не требует копирования кода          | 1. Присутствуют не во всех редакторах 2. Необходимость установки |
|    Модуль для pip    |          1. Самый полный анализ ошибок 2. Введение статистики ошибок         |       1. Необходимость установки 2. Требуется готовый файл       |
 ### 2.2. Разработать программу, которая для заданного количества значений возвращала бы список из уникальных элементов, содержащихся во входном наборе значений. Используйте упаковку и распаковку элементов.
 ```python
 def unique_seq(*base_seq):
   res = []
   for item in base_seq:
     if item in res:
       continue
     else:
       res.append(item)
   return res

print(unique_seq(1,1,2,3,4,4,6,8,8,9))
 ```
### 2.3 Реализуйте программу с реализацией работы функции zip через функцию map. С использованием сразу лямбда функции
 ```python
  def emulated_zip(*args):
    return list(map(lambda *args: args, *args))

l1 = [2,4,56, 32]
l2 = [1,3,5,6,7,8,0]
l3 = [0, 2, 4, 25]
l4 = [1232141]
print(emulated_zip(l1,l2,l3,l4))

 ```
