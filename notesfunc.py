from datetime import datetime
notesfile = open ('notes.txt', 'r')
notes = []
date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
with open('notes.txt') as fp:
        count = 0
        for count, line in enumerate(fp):
            id = count +1

def addnote ():
    with open('notes.txt') as fp:
        count = 0
        for count, line in enumerate(fp):
            id = count +1
    notes.append(id)   
    title = input('enter title: ')
    notes.append(title)
    content = input('enter content: ')
    notes.append(content)  
    notes.append(date)
    notesfile = open ('notes.txt', 'a')
    print(notes, file=notesfile)
    notesfile = open ('notes.txt', 'r')
    notesfile.readline()
    notesfile.close()

# addnote()

def show_allnotes():
    print(open('notes.txt').read())
# show_allnotes()


def show_note():
    noteid = int(input('enter note id to see a note:    '))
    for count, line in enumerate(notesfile):
        if count == noteid:
            print(count,line)
   
show_note()

# print("Do you want to change ones of the notes, type 'yes' or 'no':    ")

# answer = input()
# if answer == 'no': print('start again')
# if answer == 'yes':
#     print("What section do you want to edit, 'title' or 'content'?")
#     editanswer = input()
#     if editanswer == 'title': 
#         def edit_title


notesfile = open ('notes.txt', 'a')
def edit_title():
    noteid = (input('enter noteid: '))
    with open('notes.txt') as file:
        for line in file:
            if noteid in line:
                print(line)
                newline = list(line.split(","))
                newline[0] = id               
                newline[1] = input('enter new title: ')  
                newline[3] = date
                print(newline, file=notesfile)
                break
    notesfile.close()

           
# edit_title()



def edit_content():
    noteid = (input('enter noteid: '))
    with open('notes.txt') as file:
        for line in file:
            if noteid in line:
                print(line)
                newline = list(line.split(","))
                newline[0] = id               
                newline[2] = input('enter new content: ')  
                newline[3] = date
                print(newline, file=notesfile)
                break
            # if noteid not in line:
            #     print("all notes:")
            #     show_allnotes()
            #     edit_content()
    notesfile.close()

# edit_content()

       
def deletenotes():
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

# deletenotes()