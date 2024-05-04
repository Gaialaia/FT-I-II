
# s = "'title', 'content', '28.04.2024 13:49:15', '29'"
# s = ' '
# print(s)
# nl =  list(s.split(",")) 
# print(nl[2])
# print(nl)

# with open('notes.txt') as file:
#         for line in file:
#             linelist = list(line.split(","))
#             print(linelist[0])

# with open ('notes.csv') as file:
#     for line in file:
#         # line = list(line.split(","))
#         print(line)

file = open('notes.csv')  #every line as a list
line = file.readline()
line1 = file.readline()
line = (list(line.split(",")))
line1 = (list(line1.split(",")))   
print(line[0])
print(line1[0])








    
# file2 = open('notes.txt')
# print(file2.readline())
       


# notesfile = open ('notes.txt', 'r')  # prints based on id as id made with enumerate
# for count, line in enumerate(notesfile):
#     if count == 0:
#         print(count,line)  # должно работать если данные вводить поэтапно
    

# count = 0  
# notesfile = open ('notes.txt', 'r')  # to make every line as list so find right line on id
# line = notesfile.read()
# print(line)





    
   


    



# count = 0 # prints line count, that is different from id
# for line in notesfile:
#     count +=1
#     if count == 6:
#         print(count,line)



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


