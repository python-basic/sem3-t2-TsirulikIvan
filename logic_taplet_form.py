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
