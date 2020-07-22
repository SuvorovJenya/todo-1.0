import datetime
import json

print('          to-do list')
print('''1 - Добавить задачу
2 - Посмотреть все задачи
3 - Удалить задачу
4 - Отчистить список задач
5 - Выход''')
todoList = []
count = 1

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    todoList = data



def add(task):
	global count
	if len(todoList) == 0:
		count = 1
	todoList.append({'id': count, 
					'message': task, 
					'datetime': datetime.datetime.today().strftime("%f")})
	count += 1
	see_all_tasks()


def see_all_tasks():
	for todo in todoList:
		new_datetime = int(todo['datetime'])
		print('{}.{}\n{}'.format(
			todo['id'],
			datetime.datetime.fromtimestamp(new_datetime).today().strftime('%Y-%m-%d %H:%M'), 
			todo['message']))


def remove(idd):
	global todoList
	todoList = [todo for todo in todoList if todo['id'] != idd]
	print('Твой список выглядит так')
	see_all_tasks()


def remove_all():
	todoList.clear()
	return 'Твой список дел пуст'


while True:
	work = str(input('Что вы хотите? '))
	if work == '1':
		task = str(input('Какую задачу? '))
		add(task)
	if work == '2':
		if len(todoList) == 0:
			print('Твой список пуст')
		else:
			see_all_tasks()
	if work == '3':
		idd = int(input('Какую задачу?(id)'))
		remove(idd)
	if work == '4':
		print(remove_all())
	if work == '5':
		break

with open("data_file.json", "w") as write_file:
    json.dump(todoList, write_file)