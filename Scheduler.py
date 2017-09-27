#Scheduler alpha 0.2 (консольная версия)
#Сценарий, которй ведёт список дел
#Сценарий написан для Python3, так как новый стиль форматирования строк
#интереснее, но вероятно, целесообразно сделать и для 2.6--2.7

def tasker(task):		#создаёт строку (словарь, dikt) c заданием
    __task={'start_time':task[0], 'end_time':task[1], 'plase':task[2], 'description':task[3]}
    return __task

#class Task(list):
#    pass

print('Scheduler alpha 0.2 (консольная версия)')	#Шапка
plans  = []			#Основной список

#Основной цикл (позже, может, имеет смысл сделать его процедурой)

while True:		
    mode = input('''
Введите:
"in"  - чтобы добавить задание в список
"out" - чтобы вывести весь список
"q"   - чтобы выйти

''')

    if   mode == "in":
        task=input(
'Введите через запятую время начала, время окончания, место и название события\n'
).split(',')
        plans.append(tasker(task))
    elif mode == "out":
        print ('Весь список:\n')
        print ('{0:<20}{1:<20}{2:<20}{3:<20}'.format(
            'Время начала','Время окончания','Место','Описание'))
        for plan in plans:
            print ('{0[start_time]:<20}{0[end_time]:<20}{0[plase]:<20}{0[description]:<20}'.format(plan))
    elif mode == "q":
        break
    else: 
        print('Что-то не так')
        continue




