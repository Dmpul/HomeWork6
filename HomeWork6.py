# Работа со словарями:
my_dict = {'Dmitriy':1988, 'Polina': 1989, 'Pavel':2003, 'Platon': 1876}
print(my_dict)
print(my_dict['Polina'])# - Выведите на экран одно значение по существующему ключу,
my_dict['Igor']=1965
print(my_dict['Igor']) # одно по отсутствуещему из словаря my_dict без ошибки.
my_dict.update({'Roman':1987, 'Pavel':1992, 'Isolda': 2014}) # -Добавьте ещё две произвольные пары того же формата в словарь my_dict.
print(my_dict)
del my_dict['Igor'] #-Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(my_dict.get('Igor', 'Такого ключа не существует'))# и выведите значение из этой пары на экран.
print(my_dict) #-Выведите на экран словарь my_dict.
# Работа с множествами:
my_set={1,2,3,4,5,6,7,7,4,3,3,5,'Hold', True, 'Cool', (1,2,3,4,5)}
print(my_set)
my_set.add(9)
my_set.add(8)# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.remove(3)# Удалите один любой элемент из множества my_set.
print(my_set)# Выведите на экран измененное множество my_set.