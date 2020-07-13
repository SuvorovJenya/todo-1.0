print('------Список дел-------')
spisok_del = []
def dobavit(zadacha):
	spisok_del.append(zadacha)
	return spisok_del
def posmotret():
	return spisok_del
def udalit(zadacha):
	if zadacha in spisok_del:
		spisok_del.remove(zadacha)
		return 'Теперь твой список дел выглядит так: ',spisok_del
def udalit_all(): 
	spisok_del.clear()
	return('Твой список дел пуст)')
while True:
	delo = str(input('Что вы хотите? '))
	if delo == 'добавить задачу':
		zadacha = str(input('Какую задачу? '))
		print('Твой список дел ', dobavit(zadacha))
		continue
	if delo == 'посмотреть все задачи':
		print(posmotret())
		continue
	if delo == 'удалить задачу':
		zadacha = str(input('Какую задачу? '))
		print(udalit(zadacha))
		continue
	if delo == 'удалить все':
		print(udalit_all())
		continue
	if delo == 'посмотреть список дел':
		if len(spisok_del) == 0:
			print('Твой список дел пуст)')
		else:
			print(spisok_del)
			continue
	if delo == 'выход':
		break




