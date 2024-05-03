notesfile = open ('notes.txt', 'a')


from datetime import datetime
import random
titles = ('title', 'content', 'id', 'date')
notes = []

title = input('enter title: ')
notes.append(title)
content = input('enter content: ')
notes.append(content)
date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
notes.append(date)

# while True:
#     with open('notes.txt') as fp:
#         count = 0
#         for count, line in enumerate(fp):
#             id = count +1
#             notes.append(id)



id = random.randrange(100)
notes.append(id)
print(notes, file=notesfile)



        









