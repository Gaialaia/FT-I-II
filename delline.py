#remove line, delete a notes
notesfile = open ('notes.txt')
with open('notes.txt') as file:
    lines = file.readlines()
    print(lines[3])
    del lines[3] 
      
with open('notes.txt', "w") as file:
      for line in lines:
        file.write(line)
