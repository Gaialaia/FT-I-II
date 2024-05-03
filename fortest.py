
s = "'title', 'content', '28.04.2024 13:49:15', '29'"
# s = ' '
# print(s)
# nl =  list(s.split(",")) 
# print(nl[2])
# print(nl)

# with open('notes.txt') as file:
#         for line in file:
#             linelist = list(line.split(","))
#             print(linelist[0])



notesfile = open ('notes.txt', 'r')
for count, line in enumerate(notesfile):
    if count == 2:
        print(count,line)


# from datetime import datetime
# date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

# import json

# import csv

# rdr = csv.reader(open('notes.txt'))
# for row in rdr:
#     print(row)

# name = dict(first='bob', last='smith')
# rec = dict(name=name, job=['dev','mng'], age=40.5)

# s = json.dumps(rec)
# print(s)

# o = json.loads(s)

# o==s

# json.dump(rec,fp=open('testjson.txt', 'w'), indent=4)
# print(open('testjson.txt').read())



# p = json.load(open('notes.txt'))
# print(p)


