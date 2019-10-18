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
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About

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
  
  
