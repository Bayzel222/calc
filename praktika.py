"""
хотим калькулятор выражений -2 + 3.5 *2 - 3 ^ 2
"""

#считать строчку от пользователя
instr = input('что вычислить? ')
print(instr)

#почистить строку
# "-2 + 3.5 *2 - 3 ^ 2" -> "-2+3.5*2-3^2"
instr = instr.replace(' ', '')

#распарсить
"""
на вход строку
"-2+3.5*2-3^@"
на выход ?структура данных? с операциями +- и значениями
(+ * - ^)
("-2 3.5 2 3^2)
"""
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

#вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значений и операций
на выход обновленная структура данных

-2+3.5*2-3^2
-2+3.5*2-9
"""
actions = list()
d = dict()
d['opr'] = 'First'
d['val'] = ''
actions.append(d)

#вычислить операции второго приоритета(умнож и деление)
"""
на вход наш набор значений и операций
на выход обновленная структура данных с операциями +-

-2+3.5*2-9
-2+7-9
"""
for i, letter in enumerate(instr):
    if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
        actions.append({'opr': letter, 'val': ''})

    elif letter in digit_chars:
        actions[-1]['val'] += letter

#вычислить операции 3го приоритета (сложение и вычитание)
#-2+7-9=-4
i = 0
actions.reverse()
while i < len(actions):   
     action = actions[i]
     operation = action.get('opr')
     if operation in hp_ops:
        if operation == '^':
           pre_res = float(actions[i+1].get('val'))** float(action.get('val'))
           actions[i+1]['val'] = str(pre_res)
           del actions[i]
     else:
        i +=1
actions.reverse()

i = 0
result = '0'
error = False
while i < len(actions):
     action = actions[i]
     operation = action.get('opr')
     if operation in mp_ops:
         if float(action.get('val')) == 0 and operation == '/':
           result = 'Inf'
           error = True
         else:
           eval_str = (actions[i-1].get('val') + operation + action.get('val'))
           pre_res = eval(eval_str)
           #pre_res = eval('{0}{1}{2}'.format(float(actions[i-1].get('val')),operation,float(action.get('val'))))
           action[i-1]['val'] = str(pre_res)
         actions.pop(i)
     else:
         i += 1

var_A = ''
var_B = ''

if not error:
    for action in actions:
        var_A = result
        var_B = action.get('val')
        operation = action.get('opr')
        if operation in lp_ops:
           result = str(eval(var_A + operation + var_B))
        else:
           result = var_B
        print(result)
#вывести результат
print ('Результат: {}'.format(result))

