# Задание 1. Приложение заметки (Python)
# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента

import datetime
notes = open('notes.txt', 'a')


n = {'ID': [], 'title': ' ', 'note': ' ', 'when created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


while True:
    with open('notes.txt') as fp:
        count = 0
        for count, line in enumerate(fp):
            n['ID'] = count +1
            # pass


    n['title'] = input('enter title: \n')
    n['note'] = input('enter note \n')

    print(n.values(), file=notes, end="" "\n")
  
    break


print("Do you want to edit your note?")
answer = input("")
if "yes":

    file2 = open ('notes.txt')  #find line and can replace i.e edit
    sl = n['ID']
    for pos, lnum in enumerate(file2):
        if pos in sl:
            nl = lnum.replace(sl, '112')        
            nl =  list(lnum.split(",")) 
            n['when created'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
            print(nl, file=notesfile)






# # f = open ('notes.txt')
# # while True:
# #     line = f.read(1)
# #     if not line: break
# #     print(line)
#







