import csv


notesfile = open ('notes.csv', 'a')


from datetime import datetime


notes = []

with open('notes.csv') as fp:
     count = 0
     for count, line in enumerate(fp):
            id = count +1
notes.append(id)


title = input('enter title: ')
notes.append(title)
content = input('enter content: ')
notes.append(content)
date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
notes.append(date)



print(notes, file=notesfile)
notesfile = open ('notes.csv', 'r') #to place a carit at the end of file
notesfile.read()
notesfile.flush()
notesfile.close()

notesfile = open ('notes.txt', 'a')
print("Do you want to edit your note? ")
answer = input()
if answer == 'no': print('start again')

if answer == 'yes':
    noteid = input('enter noteid: ')
    with open('notes.txt') as file:
        for line in file:
            if noteid in line:
                print(line)
                print("What section do you want to be edited?: ")
                editanswer = input()
                if editanswer == 'content':
                    newline = list(line.split(","))
                    editanswer = newline[0]
                    newline[0] = input('enter new content: ')               
                    newline[2] = date
                    newline[3] = id
                    print(newline, file=notesfile)
                    # line = file.readline()
                    # del line([noteid])
                    # notesfile.close()
                    
                if editanswer == 'title':
                    newline = list(line.split(","))
                    editanswer = newline[1]
                    newline[0] = input('enter new title: ')               
                    newline[2] = date
                    newline[3] = id
                    print(newline, file=notesfile)
                    notesfile.close()
                break 


print("Enter notedid to remove a note")
noteid = int(input())

with open('notes.txt') as file:
    lines = file.readlines()
    print(lines[noteid])
    del lines[noteid] 
      
with open('notes.txt', "w") as file:
      for line in lines:
        file.write(line)

notesfile.close()





    
















# #     # file2 = open ('notes.txt')  #find line and can replace i.e edit
# #     # noteid = input('enter notedid ')
# #     # sl = [noteid]  # line number
# #     # for pos, lnum in enumerate(file2):
# #     #     if sl in pos:
                 
# #     #         nl =  list(lnum.split(",")) 
# #     #         nl = lnum.replace('y', 'yum') 
# #     #         nl[2] = date
# #     # print(nl, file=notesfile)

        









